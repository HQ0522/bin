from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView

#app_name = 'infor'

urlpatterns = [
    path('', views.index,name='index'),
    path('login/',views.login_view,name= 'login'),
    path('search/',views.search,name='search'),
    path('logout/',views.logout_view,name='logout'),
    path('register/',views.register,name='register'),
    path('recommend/',views.recommend,name='recommend'),
    path('favor/',views.favor,name='favor'),
]