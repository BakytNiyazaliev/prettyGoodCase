from django.urls import path, re_path


from .views import menu_list, menu_detail


app_name = 'tree_menu'

urlpatterns = [
    path('', view=menu_list, name='menu_list'),
    path('<str:name>', view=menu_detail, name='menu_detail'),
    path('<str:head_name>/<int:level>/<str:name>', menu_detail, name='menu_item')
]