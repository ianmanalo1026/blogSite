from blogger.models import BlogPost
from django.forms import ModelForm
from .models import BlogPost

class CreateBlogForm(ModelForm):
    class Meta:
        model = BlogPost
        fields = ['blog_title','blog_content']