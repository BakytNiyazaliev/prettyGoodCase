from django.shortcuts import render

from .models import Node

def menu_list(request):
    if request.method == 'GET':
        nodes = Node.objects.filter(parent__isnull=True)
        return render(request, "menu/menu_list.html",{'nodes': nodes})
    

def menu_detail(request, name, head_name='', level=0):
    if request.method == 'GET':
        node = Node.objects.get(name=name)
        return render(request, "menu/menu_detail.html", {'node':node})