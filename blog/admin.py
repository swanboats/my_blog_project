from django.contrib import admin
from .models import Post, SiteSetting, Profile

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')
    search_fields = ('title', 'content')

@admin.register(SiteSetting)
class SiteSettingAdmin(admin.ModelAdmin):
    list_display = ('site_title',)

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('name',)
