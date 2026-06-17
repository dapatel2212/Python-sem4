from django.shortcuts import render
from django.http import HttpResponse
from . models import Student
data = [{"Rollno":1,"Name":"Abc"},{"Rollno":2,"Name":"Def"},{"Rollno":3,"Name":"Gh1"}]
def home(request):
    return render(request,"home.html")
# Create your views here.
def rooms(request):
    dt = Student.objects.all()
    return render(request, 'rooms.html', {'data': dt})
