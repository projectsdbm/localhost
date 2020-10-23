from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from .forms import StudentCreateForm
from django.contrib.auth.decorators import login_required
from student.models import StudentModel, DepartmentModel
# Create your views here.

#login the teacher
def TeacherLoginView(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('/teacher')
        else:
            return HttpResponse('unable  to login')
    return render(request,'teacher/login.html',{})


#log out the teacher
def TeacherLogoutView(request):
    logout(request)
    return redirect('/teacher')

#just some empty pages
def TeacherHomeView(request):
    return render(request,'teacher/teacherhome.html',{})


def select(request):
    return render(request,'homepage.html',{})

#add student
@login_required(login_url='/teacher/login')
def StudentAddView(request):
    form = StudentCreateForm()
    if request.method == "POST":
        form = StudentCreateForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse('student added')
        else:
            print(form.errors)
            return HttpResponse('Some error')

    return render(request,'teacher/studentadd.html',{"form":form})



#search list of all the student
@login_required(login_url='/teacher/login')
def StudentListView(request):
    if request.method=="POST":
        Class_name = request.POST['classname']
        year = request.POST['year']
        department = request.POST['department']
        dep = DepartmentModel.objects.get(dept_name=department)
        users = StudentModel.objects.filter(Class=Class_name,year=year,department=dep)
        return render(request,'teacher/studentdetail.html',{'users':users,"dept":department,"class":Class_name,"year":year})
    return render(request,'teacher/search.html',{})

#search detail of particular student
@login_required(login_url='/teacher/login')
def StudentDetialView(request):
    if request.method == "POST":
        roll_no = request.POST['roll_no']
        user = StudentModel.objects.filter(roll_no=roll_no)
        return render(request,'teacher/studentfulldet.html',{"student":user[0]})
    return render(request,'teacher/studentsearch.html',{})


#delete a student
def StudentDeleteView(request,id):
    user = StudentModel.objects.get(id=id)
    user.delete()
    return HttpResponse('Deleted Successfuly')
