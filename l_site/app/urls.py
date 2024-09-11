from django.urls import path

from app import views

urlpatterns = [
    path('', views.about, name="about"),
    path('home/', views.home, name="home"),
    path('contacts/', views.contacts, name="contacts")
]