from django.db import models
from django.contrib.auth.models import User

class BlogPost(models.Model):
    blog_title = models.CharField(max_length=250)
    blog_content = models.TextField(blank=True)
    blog_publish = models.DateTimeField(auto_now_add=True)
    blog_user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.blog_title
    
