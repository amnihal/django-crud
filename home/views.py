from django.shortcuts import render
from . models import Marklist

# Create your views here.


def index(request):
    if request.method=="POST":

        student = Marklist()
        
        student.name = request.POST.get('name')
        student.rollno = request.POST.get('rollno')
        student.grade = request.POST.get('grade')

        student.save()

    student=Marklist.objects.all()

    student = {
        "student":student
    }
    
    return render(request,'index.html',student)


