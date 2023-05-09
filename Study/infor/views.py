from django.shortcuts import render,HttpResponse,redirect
from .models import Course
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

from django.contrib.auth import get_user_model

User = get_user_model()



from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm,RegisterForm


# Create your views here.
def index(request):
    courses = Course.objects.all()
    paginator = Paginator(courses, 6)  # Show 6 contacts per page.
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(request,'infor/index.html',locals())


def search(request):
    query = request.GET.get('query')
    if query is None or query.strip() == '':
        courses = []  # 如果搜索关键字为空，返回空结果
    else:
        courses = Course.objects.filter(title__icontains=query)

    paginator = Paginator(courses, 6)  # Show 6 courses per page
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(request, 'infor/search.html', {'page_obj': page_obj, 'query': query})


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirect to a success page
            return redirect('success')
            print('成功了吗')
        else:
            error_message = '用户名或密码不正确'
            return render(request, 'infor/login.html', {'error_message': error_message})
    else:
        return render(request, 'infor/login.html')



def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('home')
    else:
        form = RegisterForm()
    return render(request, 'infor/register.html', {'form': form})


def logout(request):
    logout(request)
    return redirect('home')

@login_required
def recommend1(requst):
    return render(requst,'infor/recommend1')
#infor/inforlist.html

from django.contrib import messages


