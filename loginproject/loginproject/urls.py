from django.contrib import admin
from django.urls import path
from accounts import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.user_login, name="login"),
    path("home/", views.home, name="home"),
]