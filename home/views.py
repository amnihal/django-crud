from django.shortcuts import render , redirect
from . models import Marklist


# Create your views here.


def post_mark(request):
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

def update_mark(request,id):
    stud = Marklist.objects.get(id=id)
    if request.method=="POST":
        
        stud.name = request.POST['name']
        stud.rollno = request.POST['rollno']
        stud.grade = request.POST['grade']
        stud.save()

        return redirect('post_mark')
    
    stud = {
        "stud" : stud
    }

    return render(request,'update.html',stud)

def remove_mark(request,id):
    stud = Marklist.objects.get(id=id).delete()

    return redirect('post_mark')






