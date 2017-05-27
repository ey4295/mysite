import re

from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db import connections
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from pandas import json
from pymongo import MongoClient

from blog.forms import PostForm, SendMessage
from blog.models import Post, User_Request
from blog.tools.analyse_tools import get_entities, get_tokens, get_pos, get_sentiment
from blog.tools.send_messages import send_text


def test(request):
    """
    test page
    :param request:
    :return:
    """
    return render(request, 'blog/test.html')


def register_visitor(request):
    req = User_Request()
    req.path = request.path;
    req.REMOTE_ADDR = request.META["REMOTE_ADDR"]
    req.store()


def posts_list(request):
    register_visitor(request)
    posts = Post.objects.all().order_by("-created_date")
    return render(request, 'blog/posts_list.html', {'posts': posts, })


def posts_detail(request, pk):
    register_visitor(request)
    post = Post.objects.get(pk=pk)
    return render(request, 'blog/posts_detail.html', {'post': post, })


def heatmap(request):
    register_visitor(request)
    return render(request, 'blog/Heatmap.html', {})


def usermap(request):
    register_visitor(request)
    return render(request, 'blog/Usermap.html', {})


def current_user(request):
    requests = User_Request.objects.all()
    IPs = [req.REMOTE_ADDR for req in requests]
    IPs = {}.fromkeys(IPs).keys()
    total = len(IPs)
    register_visitor(request)
    return render(request, 'blog/Current_user.html', {'total': total, })


@login_required
def writePost(request):
    """
    provide interface for adding new post&&save new post
    :param request:
    :return:a template with form
    """
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.publish()
            return redirect('posts_detail', pk=post.pk)
    else:
        register_visitor(request)
        # form=CharField(widget=FroalaEditor)
        form = PostForm()
        # form=FroalaEditor()
    return render(request, 'blog/writePost.html', {'form': form})  # FIXIT


@login_required
def editPost(request, pk):
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


@login_required()
def sendmsg(request):
    """
    send a message to cellphones
    :param request: post or get
    :return: void
    """
    if request.method == "POST":
        form = SendMessage(request.POST)
        if form.is_valid():
            msg = form.save(commit=False)
            to_cell = "+86{0}".format(msg.to_cell)
            content = msg.content
            msg.store()
            try:
                print (to_cell)

                send_text(to_cell=str(to_cell), message=str(content))

                return redirect('success')
            except Exception as err:
                request.session['st'] = str(err)
                return redirect('failure')

    else:
        form = SendMessage()
        return render(request, 'blog/send_msg.html', {'form': form})


def failure(request):
    """
    responde a failure page
    :param request:
    :return: void
    """
    return render(request, 'blog/failure.html', {'error': request.session.get('st')})


def success(request):
    """
    responde a success page
    :param request:
    :return: void
    """
    return render(request, 'blog/success.html')


########################################################################################################
# Graduation Project Result Display
#   1.Named entity Analysis
#   2.Sentiment Analysis
#   3.DataBase Display
########################################################################################################

def ner(request):
    """
    Named Entity Recognition Page
    :param request: web request
    :return: template
    """
    return render(request, 'blog/ner.html')


def ner_process(request):
    """
    process sentence and analyse it ,return result as JSON
    :param request:
    :return:
    """
    result = {}
    try:
        sent = request.POST['sentence']

        result['tokens'] = get_tokens(sent)
        result['pos'] = get_pos(sent)
        result['ner_dict'] = get_entities(sent)
    except Exception as err:
        f=open('my.log')
        f.write(err)
        f.close()
    return JsonResponse({'result': result})


def sentiment(request):
    """
    conduct sentiment analysis
    :param request:
    :return: page
    """
    return render(request, 'blog/sentiment.html')


def sentiment_process(request):
    """
    conduct sentiment process
    :return: JSON data
    """
    sent = request.POST['sentence']
    return JsonResponse(get_sentiment(sent))


def get_activity(request):
    """
    get activity from mysql db
    :param request:
    :return:
    """
    connection = connections['people_mysql']
    cursor = connection.cursor()
    sql = 'select activity_id,name_list.name,activity.PERSON,activity.VB ,activity.ORGANIZATION,activity.LOCATION,activity.DATE from name_list, activity where name_list.person_id=activity.person_id;'
    cursor.execute(sql)
    result = cursor.fetchall()
    paginator = Paginator(result, 25)  # Show 25 contacts per page

    page = request.GET.get('page')
    try:
        activities = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        activities = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        activities = paginator.page(paginator.num_pages)

    return render(request, 'blog/activity.html', {'activities': activities})


def get_property(request):
    """
    get structured property from request
    :param request:
    :return:
    """
    client = MongoClient()
    db = client.people
    properties = db.properties
    properties = properties.find()
    result = []
    for p in properties:
        try:
            p = json.dumps(p)
            result.append(p)
        except Exception as err:
            continue

    paginator = Paginator(result, 2)  # Show 25 contacts per page
    page = request.GET.get('page')
    try:
        properties = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        properties = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        properties = paginator.page(paginator.num_pages)
    return render(request, 'blog/property.html', {"properties": properties})
