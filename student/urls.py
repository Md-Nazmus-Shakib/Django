from django.contrib import admin
from django.urls import path,include
from .import views

urlpatterns = [
    # path('home/', views.home, name='home'),
    path('home/', views.CreateStudentView.as_view(), name='home'),
    # path('data/',views.showdata,name="data"),
    path('data/',views.StudentListView.as_view(),name="data"),
    #path('delete/<int:unique_ID>/',views.delete_student,name="delete_student"),
    path('delete/<int:unique_ID>/',views.DeleteStudentView.as_view(),name="delete_student"),
    # path('edit/<int:unique_ID>/',views.edit_student,name="edit_student"),
    path('edit/<int:unique_ID>/',views.UpdateStudentView.as_view(),name="edit_student"),
]