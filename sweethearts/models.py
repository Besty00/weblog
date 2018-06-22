from django.db import models

# Create your models here.


class Article(models.Model):
    title = models.CharField(max_length=50, null=False)
    text = models.TextField(null=False)
    pubDate = models.DateField(auto_now=True, null=False)

    def __repr__(self):
        return "<Article: %s>" % self.title

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "记 录"
