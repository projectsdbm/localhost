from django.shortcuts import render
from .models import StudentModel
from django.http import HttpResponse
# Create your views here.

def StudentSearchView(request):
    user = None
    if request.method == "POST":
        roll_no = request.POST['rollno']
        password = request.POST['password']
        student = StudentModel.objects.filter(roll_no=roll_no)
        print(student)
        if len(student) != 0:
            if student[0].password == password:
                user = student[0]
                return render(request,'student/details.html',{"student":user})
            else:
                return render(request,'student/search.html',{"Error":True})
        else:
            return render(request,'student/search.html',{"Error":True})
    return render(request,'student/search.html',{})
