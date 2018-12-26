from django.conf.urls import url
from django.contrib import admin
from core import views

urlpatterns = [
    url('', views.home, name="home"),
    url('/about/', views.about, name="about"),
    url(r'^admin/', admin.site.urls),
]
