from django.db import models
import os
import uuid

def student_directory_name(instance,filename):
    unique_folder = str(uuid.uuid4())[:6]
    return os.path.join('student/media',instance.name+"_"+unique_folder,filename)

# Create your models here.
class student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=254, unique=True)
    age = models.PositiveIntegerField()
    unique_ID = models.PositiveIntegerField(primary_key=True,unique=True,null=False,blank=False)
    password = models.CharField(max_length=8)
    checkbox = models.BooleanField(default=False)
    photo = models.ImageField(upload_to=student_directory_name)
    
    def __str__(self):
        return f"{self.name}"
