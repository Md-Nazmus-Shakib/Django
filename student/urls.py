from django.contrib import admin
from django.urls import path,include
from .import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('data/',views.showdata,name="data"),
    path('delete/<int:unique_ID>/',views.delete_student,name="delete_student"),
    path('edit/<int:unique_ID>/',views.edit_student,name="edit_student"),
]