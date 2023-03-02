from django import template

from ..models import Node

register = template.Library()

@register.inclusion_tag("menu/draw_menu.html")
def draw_menu(name: str, tail_name=''):
    node = Node.objects.get(name=name)
    nodes_to_open = []
    item = node
    while item:
        nodes_to_open.append(item.name)
        item = item.parent
    head = Node.objects.get(name=node.get_head_name())
    return {'node': head, 'nodes_to_open':nodes_to_open}