from django.urls import path
from django.contrib import admin
from core import views

urlpatterns = [
    path('', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('admin/', admin.site.urls),
]
