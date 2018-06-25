from django.db import models

# Create your models here.


class Article(models.Model):
    title = models.CharField(max_length=50, null=False, verbose_name=u'标题')
    text = models.TextField(null=False, verbose_name=u'正文')
    abstract = models.TextField(null=False, verbose_name=u'摘要',max_length=40)
    pubDate = models.DateField(auto_now=True, null=False, verbose_name=u'发布日期')

    def __repr__(self):
        return "<Article: %s>" % self.title

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "记 录"


class Guestbook(models.Model):
    msg = models.TextField(null=False)

