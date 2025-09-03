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
