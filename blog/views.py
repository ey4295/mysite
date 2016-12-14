from time import timezone

from django.contrib.auth.decorators import login_required
from django.forms import CharField
from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from froala_editor.widgets import FroalaEditor

from blog.forms import PostForm
from blog.models import Post, User_Request

def register_visitor(request):
    req = User_Request()
    req.path = request.path;
    req.REMOTE_ADDR = request.META["REMOTE_ADDR"]
    req.store()

def posts_list(request):
    register_visitor(request)
    posts=Post.objects.all().order_by("-created_date")
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

@login_required
def writePost(request):
    """
    provide interface for adding new post&&save new post
    :param request:
    :return:a template with form
    """
    if request.method=="POST":
        form=PostForm(request.POST)
        if form.is_valid():
            post=form.save(commit=False)
            post.publish()
            return redirect('posts_detail',pk=post.pk)
    else:
        register_visitor(request)
        #form=CharField(widget=FroalaEditor)
        form=PostForm()
        #form=FroalaEditor()
    return render(request, 'blog/writePost.html', {'form':form})#FIXIT

@login_required
def editPost(request,pk):
    """
    get original post &&& save edit
    :param request:Http request send by user
    :return: template
    """
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.publish()
            return redirect('posts_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/editPost.html', {'form': form})