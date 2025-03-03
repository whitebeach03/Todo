from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('add/', views.add_todo, name='add_todo'),
    path('complete/<int:todo_id>/', views.complete_todo, name='complete_todo'),
    path('delete/<int:todo_id>/', views.delete_todo, name='delete_todo'),
]
