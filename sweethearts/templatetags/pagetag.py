# -*-coding:utf-8 -*-

from django import template
from django.utils.html import format_html

register = template.Library()


@register.simple_tag
def circle_page(curPage, loopPage):
    offset = abs(curPage - loopPage)
    if offset < 3:
        if curPage == loopPage:
            page_ele = '<li class="active"><a href="?page=%s">%s</a></li>' % (loopPage,loopPage)
        else:
            page_ele = '<li><a href="?page=%s">%s</a></li>' % (loopPage, loopPage)
        return format_html(page_ele)
    else:
        return ''
