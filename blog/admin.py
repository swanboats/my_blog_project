from django.contrib import admin
from .models import Post, SiteSetting

admin.site.register(Post)
admin.site.register(SiteSetting)
