from django.db import models

# Create your models here.
class Post(models.Model):
    '''
    投稿モデル
    '''
    title = models.CharField()
    body = models.TextField()
