from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ImageField(upload_to='post_images/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class SiteSetting(models.Model):
    site_title = models.CharField(max_length=200, default='My Blog')
    header_image = models.ImageField(upload_to='site_images/')

    def __str__(self):
        return self.site_title

class Profile(models.Model):
    name = models.CharField(max_length=100, verbose_name="名前")
    bio = models.TextField(verbose_name="プロフィール文", blank=True)
    icon = models.ImageField(upload_to='profile_icons/', verbose_name="プロフィール画像", blank=True, null=True)

    def __str__(self):
        return self.name