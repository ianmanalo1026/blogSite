from django.contrib import admin
from blogger.models import BlogPost


class BlogPostAdmin(admin.ModelAdmin):
    readonly_fields = ('blog_publish',)

admin.site.register(BlogPost, BlogPostAdmin)
