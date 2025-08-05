from django.db import models

# Create your models here.

from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=200)  # 記事のタイトル
    content = models.TextField()              # 記事の内容
    created_at = models.DateTimeField(auto_now_add=True)  # 作成日時
    updated_at = models.DateTimeField(auto_now=True)      # 更新日時

    def __str__(self):
        return self.title
