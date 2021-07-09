from django.contrib import admin
from .models import Profile, BlogPosts

admin.site.register(BlogPosts)


class ProfileAdmin(admin.ModelAdmin):
    pass

admin.site.register(Profile, ProfileAdmin)
