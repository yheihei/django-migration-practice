from django.db import models

# Create your models here.
class Post(models.Model):
    '''
    投稿モデル
    '''
    title = models.CharField(max_length=255)
    body = models.TextField()


class Comment(models.Model):
    '''
    投稿に紐つくコメント
    '''
    post = models.ForeignKey(
        'Post',
        on_delete=models.CASCADE
    )
    user_name = models.CharField(max_length=255)
    body = models.TextField()
