import os
from django.contrib import messages
from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpResponseRedirect
from . import models
from .import forms
from django.views.generic import ListView
from django.views.generic import UpdateView , DeleteView,CreateView
from django.urls import reverse_lazy

class CreateStudentView(CreateView):
    # model = models.student
    form_class= forms.studentForm
    template_name = 'student/index.html'
    success_url = reverse_lazy('home')
    def form_valid(self, form):
        """If the form is valid, save the associated model."""
        # self.object = form.save()
        messages.add_message(self.request, messages.SUCCESS, 'Form submitted successfully.')
        return super().form_valid(form)#this saves automatically


class StudentListView(ListView):
    model = models.student
    template_name = 'student/data.html'
    context_object_name = 'student_data'
    
    

class UpdateStudentView(UpdateView):
    model = models.student
    form_class =forms.studentForm
    template_name = 'student/index.html'
    pk_url_kwarg = 'unique_ID' #to tell which field is primary key in url
    success_url = reverse_lazy('data')#work like redirect after successful updation
    def form_valid(self, form):
        """If the form is valid, save the associated model."""
        #self.object = form.save()#manually save no need
        messages.add_message(self.request, messages.SUCCESS, 'Editted successfully.')
        return super().form_valid(form) # it save automatically if i donnt call it then we caan save manually

    def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            context["edit"] = True 
            return context
        
        
        
class DeleteStudentView(DeleteView):
        model = models.student
        template_name = 'G:/Jango2/school_management/student/templates/student/delete.html'
        pk_url_kwarg = 'unique_ID'
        success_url = reverse_lazy('data')
        def delete(self, request, *args, **kwargs):
                self.object = self.get_object()
                if self.object.photo and os.path.isfile(self.object.photo.path):
                    os.remove(self.object.photo.path)
                
                messages.add_message(request, messages.SUCCESS, 'Student deleted successfully.')
                return super().delete(self.request, *args, **kwargs)
        
# Create your views here.
# def home(request):
   
#     if request.method == 'POST':
#         name = request.POST.get('name')
#         email = request.POST.get('email')
#         password = request.POST.get('password')
#         checkbox = request.POST.get('checkbox')
#         photo = request.FILES.get('photo')
#         if checkbox == 'on':
#             checkbox = True
#         else:
#             checkbox = False
#         student_data= models.student(name=name,email=email,password=password,checkbox=checkbox,photo=photo) #create object of model
#         student_data.save()
#         student_data = models.student.objects.all()
#         print(student_data)
#         return render(request,'student/index.html',{"student_data":student_data})
#     return render(request,'student/index.html')

# def home(request):
   
#     if request.method == 'POST':
#         form = forms.studentForm(request.POST,request.FILES)
#         if form.is_valid():
#             form.save()
#             messages.add_message(request, messages.SUCCESS, 'Form submitted successfully.')
#             return redirect('home')
        
#     else:
#         form = forms.studentForm()
#     return render(request,'student/index.html',{ 'form':form})
# class CreateStudentView(CreateView):
#fuinction based view
# def showdata(request):
#     query = request.GET.get('q')
#     if query :
#         student_data = models.student.objects.filter(name__icontains=query)
#     else:
        
#         student_data = models.student.objects.all()
#     return render(request,'student/data.html',{"student_data":student_data})
#class based view
# def delete_student(request,unique_ID):
#     student = models.student.objects.get(unique_ID=unique_ID)
#     student.delete()
#     student.photo.delete(save=False)  # Delete the associated photo file
#     messages.add_message(request, messages.SUCCESS, 'Student deleted successfully.')
#     return redirect('data') 
    # return HttpResponse("Student deleted successfully") #
# def edit_student(request,unique_ID): #edit function based view
#     student = models.student.objects.get(unique_ID=unique_ID)
#     form = forms.studentForm(instance=student)
#     if request.method == 'POST':
#         form = forms.studentForm(request.POST,request.FILES,instance=student)
#         if form.is_valid():
#             form.save()
#             messages.add_message(request, messages.SUCCESS, 'Editted successfully.')
#             return redirect('data')
#     return render(request,'student/index.html',{'form':form ,'edit': True})