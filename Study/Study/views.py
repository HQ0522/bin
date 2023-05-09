from django.shortcuts import render
from infor.models import Course

def index(request):
    return render(request,'index.html')

def course_list(request):
    courses = Course.objects.all()
    return render(request, 'index.html', {'courses': courses})
