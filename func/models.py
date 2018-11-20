from django.db import models

# Create your models here.
class Func(models.Model):
    text = models.TextField(default='文章正文')
