# blog/models.py
from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=200)  # 記事タイトル
    content = models.TextField()              # 記事本文
    created_at = models.DateTimeField(auto_now_add=True)  # 作成日時
    updated_at = models.DateTimeField(auto_now=True)      # 更新日時

    def __str__(self):
        return self.title

