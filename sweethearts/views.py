from django.shortcuts import render
from .models import Article
# # Create your views here.


def index(request):
    arts = Article.objects.all()
    return render(request, 'index.html', {'arts': arts})


def article(request, id):
    art = Article.objects.get(id=id)
    return render(request, 'article.html', {'art': art})

def guestbook(request):
    return render(request, 'guestbook.html')
