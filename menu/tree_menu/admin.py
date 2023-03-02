from django.contrib import admin

from .models import Node

@admin.register(Node)
class NodeAdmin(admin.ModelAdmin):
    list_display = ['name', 'parent', 'depth']
    lsit_filter = ['parent']