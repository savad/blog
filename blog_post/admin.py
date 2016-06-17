from django.contrib import admin

from blog_post.models import Blog, Tag

admin.site.register(Blog)
admin.site.register(Tag)
