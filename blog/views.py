from django.shortcuts import render

# Create your views here.
from blog.models import Post


def posts_list(request):
    posts=Post.objects.all()
    return render(request,'blog/posts_list.html',{'posts':posts,})

def posts_detail(request,pk):
    post=Post.objects.get(pk=pk)
    return render(request,'blog/posts_detail.html',{'post':post,})