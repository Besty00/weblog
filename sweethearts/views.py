from django.shortcuts import render
from .models import Article, Guestbook
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# # Create your views here.


def index(request):
    arts = Article.objects.all()
    return render(request, 'index.html', {'arts': arts})


def article(request, id):
    art = Article.objects.get(id=id)
    return render(request, 'article.html', {'art': art})

def guestbook(request):
    if request.method == 'POST':
        gb = request.POST
        name = gb['name']
        msg = gb['message']
        Guestbook.objects.create(name=name, mssge=msg)
        return render(request, 'guestbook.html')
    gbs = Guestbook.objects.all()
    paginator = Paginator(gbs, 10)
    page = request.GET.get('page')
    if page:
        gbs = paginator.page(page).object_list
    else:
        gbs = paginator.page(1).object_list
    try:
        contacts = paginator.page(page)
    except PageNotAnInteger:
        # 如果page不是一个整数，则展示第一页。
        contacts = paginator.page(1)
    except EmptyPage:
        # 如果page不在范围内（例如，9999），则展示结果的最后一页。
        contacts = paginator.page(paginator.num_pages)

    return render(request, 'guestbook.html', {'gbs': gbs, 'contacts': contacts, 'pObj': paginator})
