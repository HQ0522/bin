from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView

#app_name = 'infor'

urlpatterns = [
    path('', views.index,name='index'),
    path('login/',LoginView.as_view(template_name='infor/login.html'),name= 'login'),
    path('search/',views.search,name='search'),
    path('logout/',LogoutView.as_view(),name='logout'),
    path('register/',views.register,name='register'),
]