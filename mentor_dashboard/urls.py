from django.urls import path
from . import views


urlpatterns = [
    path("", views.dashboard, name='home'),
    path("profile/", views.updateProfile, name='Profile_update'),
    path("agree/<int:id>", views.agree, name='agree'),
    path("decline/<int:id>", views.decline, name= 'decline'),
]