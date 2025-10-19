from django.shortcuts import redirect, render
from django.http import HttpResponse
from . import models
from .import forms

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

def home(request):
   
    if request.method == 'POST':
        form = forms.studentForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse("Data saved successfully")
        
    else:
        form = forms.studentForm()
    return render(request,'student/index.html',{ 'form':form})
def showdata(request):
    query = request.GET.get('q')
    if query :
        student_data = models.student.objects.filter(name__icontains=query)
    else:
        
        student_data = models.student.objects.all()
    return render(request,'student/data.html',{"student_data":student_data})
    
def delete_student(request,unique_ID):
    student = models.student.objects.get(unique_ID=unique_ID)
    student.delete()
    student.photo.delete(save=False)  # Delete the associated photo file
    return redirect('data') 
    # return HttpResponse("Student deleted successfully")
def edit_student(request,unique_ID):
    student = models.student.objects.get(unique_ID=unique_ID)
    form = forms.studentForm(instance=student)
    if request.method == 'POST':
        form = forms.studentForm(request.POST,request.FILES,instance=student)
        if form.is_valid():
            form.save()
            return redirect('data')
    return render(request,'student/index.html',{'form':form ,'edit': True})
