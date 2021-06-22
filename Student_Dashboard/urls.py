from django.urls import path
from . import views


urlpatterns = [
    path("", views.dashboard, name='home'),
    path("profile/", views.updateProfile),
    path("qualification/", views.updateQualification),
    path("semester/", views.semester),
    path("skill/", views.skill),
    path("project/", views.project),
    path("hobby/", views.hobby),
    path("read/<int:id>",views.notice),
]