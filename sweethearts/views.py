from django.shortcuts import render
from .models import Article
# # Create your views here.
#
#
def index(request):
    arts = Article.objects.all()
    return render(request, 'index.html', {'arts': arts})
