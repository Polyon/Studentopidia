from django.urls import path
from SPT07 import views


urlpatterns = [
    path("", views.index, name='home'),
    path("students", views.student, name='students'),
    path("about", views.about, name='aboutUs'),
    path("contact", views.contact, name='contactUs'),
    path("signup", views.reg, name='registration'),
    path("signin", views.user_login, name='login'),
    path("signout", views.user_logout, name='logout'),
    path("getPassword",views.getPassword, name= 'getPassword')
]