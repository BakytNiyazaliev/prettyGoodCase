from django.db import models
from django.urls import reverse


class Node(models.Model):
    name = models.CharField(max_length=200)
    parent = models.ForeignKey('self',
                               on_delete=models.CASCADE,
                               null=True,
                               blank=True)

    def get_children(self):
        return Node.objects.filter(parent=self)

    def get_absolute_url(self):
        if not self.parent:
            return reverse("tree_menu:menu_detail", kwargs={'name': self.name})
        
        head = Node.objects.get(name=self.get_head_name()) 
        return reverse('tree_menu:menu_item',
                       kwargs={
                           'head_name': head,
                           'level': self.get_level(),
                           'name': self.name
                       })
    
    def get_head_name(self):
        if self.parent is None:
            return self.name
        head = self.parent
        while head.parent:
            head = head.parent
        return head.name

    def get_level(self):
        if not self.parent:
            return 0
        return 1 + self.parent.get_level()
    
    depth = models.IntegerField(editable=False, blank=True, null=True)

    def get_adjacent_nodes(self):
        if self.parent:
            adjacent_nodes = Node.objects.filter(parent=self.parent)
            return adjacent_nodes
        return []

    def __str__(self) -> str:
        return self.name

    def save(self, *args, **kwargs):
        self.depth = self.get_level()
        if (self.parent == self):
            raise ValueError
        super().save(*args, **kwargs)