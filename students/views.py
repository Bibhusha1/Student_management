from django.shortcuts import render,redirect
from django.urls import reverse
from.import models
# Create your views here.

def listing(request):
    students = models.Student.objects.all()
    return render(request,'list.html',{"students":students})

def delete(request):
    if request.method =='POST':
       id = request.POST['id']

       s1=models.Student.objects.filter(pk=id)
       if len(s1) ==0:
           print("no student found")
           
       else:
           s1[0].delete()
    

  
       return redirect(reverse('students:listing'))
  

    return render(request,'del.html')


def add(request):
   if request.method =='POST':
       student_name = request.POST['student_name']
       gender= request.POST['gender']
       dob= request.POST['dob']
       grade= request.POST['grade']
       semester= request.POST['semester']
       email= request.POST['email']
       phone= request.POST['phone']
       address= request.POST['address']

       models.Student.objects.create(name=student_name, gender=gender, dob=dob, grade=grade, semester=semester,emailid=email, phone=phone, address=address)

       return redirect(reverse('students:listing'))
   return render(request,'add.html')


def edit(request):
    return redirect(request,'edit.html')

