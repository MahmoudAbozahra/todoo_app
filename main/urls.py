from django.urls import path
from . import views

urlpatterns = [
   path('',views.todo_list,name='todo_list'),
   path('add/' , views.add_task , name='add_task'),
   path('del/<int:id>/',views.delete_task , name='delete_task'),
   path('edit/<int:id>/',views.edit_task,name='edit_task'),
]