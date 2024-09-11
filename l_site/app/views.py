from django.shortcuts import render

# Create your views here.


def about(request):
    return render(request, "app/about.html")

def home(request):
    return render(request, "app/home.html")

def contacts(request):
    return render(request, "app/contacts.html")
