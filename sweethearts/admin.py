# -*-coding:utf-8-*-

from django.contrib import admin
from .models import Article,Guestbook

# Register your models here.


class ArticleAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['title']}),
        ('摘要', {'fields': ['abstract']}),
        ('正文', {'fields': ['text']}),
    ]

    list_display = ('title', 'pubDate')


class GuestbookAdmin(admin.ModelAdmin):
    fieldsets = [
        ('访客', {'fields': ['name']}),
        ('留言', {'fields': ['mssge']}),
    ]

    list_display = ('name', 'mssge', 'gbtime')

admin.sites.site_header = "会 长 大 の 幸 福"
admin.sites.site_title = "会 长 大 の 幸 福"
admin.site.register(Article, ArticleAdmin)
admin.site.register(Guestbook, GuestbookAdmin)