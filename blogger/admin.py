from django.contrib import admin
from blogger.models import BlogPost, Profile


class BlogPostAdmin(admin.ModelAdmin):
    readonly_fields = ('blog_publish',)

admin.site.register(BlogPost, BlogPostAdmin)
admin.site.register(Profile)
