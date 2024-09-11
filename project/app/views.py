from django.shortcuts import render

from app.models import Article


# Create your views here.

def index(request):
    articles = Article.objects.all()
    data = {
        "articles":articles
    }
    return render(request, 'app/index.html', data)

