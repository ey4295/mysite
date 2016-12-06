from django.shortcuts import render

# Create your views here.
from blog.models import Post, User_Request

def register_visitor(request):
    req = User_Request()
    req.path = request.path;

    req.REMOTE_ADDR = request.META["REMOTE_ADDR"]
    req.store()
def posts_list(request):
    register_visitor(request)
    posts=Post.objects.all()
    return render(request,'blog/posts_list.html',{'posts':posts,})

def posts_detail(request,pk):
    register_visitor(request)
    post=Post.objects.get(pk=pk)
    return render(request,'blog/posts_detail.html',{'post':post,})

def heatmap(request):
    register_visitor(request)
    return render(request,'blog/Heatmap.html',{})

def usermap(request):
    register_visitor(request)
    return render(request,'blog/Usermap.html',{})

def current_user(request):
    requests=User_Request.objects.all()
    IPs=[req.REMOTE_ADDR for req in requests ]
    IPs={}.fromkeys(IPs).keys()
    total=len(IPs)
    register_visitor(request)
    return render(request,'blog/Current_user.html',{'total':total,})