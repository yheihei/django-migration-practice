from django.db import models

# Create your models here.
class Post(models.Model):
    '''
    投稿モデル
    '''
    title = models.CharField(max_length=255)
    body = models.TextField()
