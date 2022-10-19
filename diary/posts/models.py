from django.db import models

# Create your models here.
class Post(models.Model):
    '''
    投稿モデル
    '''
    title = models.CharField(max_length=255)
    body = models.TextField()


class Category(models.Model):
    '''
    カテゴリ
    '''
    post = models.ForeignKey(
        'Post',
        on_delete=models.CASCADE
    )
    name = models.CharField(max_length=255)
