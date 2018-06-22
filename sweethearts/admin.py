# -*-coding:utf-8-*-

from django.contrib import admin
from .models import Article

# Register your models here.


class ArticleAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['title']}),
        ('正文', {'fields': ['text']}),
    ]

    list_display = ('title','abstract','pubDate')


admin.sites.site_header = "会 长 大 の 幸 福"
admin.sites.site_title = "会 长 大 の 幸 福"
admin.site.register(Article, ArticleAdmin)