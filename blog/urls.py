import django
from django.conf.urls import url, include


from blog import views

urlpatterns=[
    url(r'^heatmap$',views.heatmap,name='heatmap'),
    url(r'^usermap$',views.usermap,name='usermap'),
    url(r'^current_user$',views.current_user,name='current_user'),
    url(r'^$',views.posts_list,name='posts_list'),
    url(r'^post/(?P<pk>\d+)/$',views.posts_detail,name='posts_detail'),
    url(r'^post/write$',views.writePost,name='writePost'),
    url(r'^post/(?P<pk>\d+)/edit/$', views.editPost, name='editPost'),
    url(r'^sendmsg$',views.sendmsg,name='sendmsg'),
    url(r'^success$',views.success,name='success'),
    url(r'^failure$',views.failure,name='failure'),
    url(r'^froala_editor/', include('froala_editor.urls')),

    #url(r'^usermap',views.posts_list,name='posts_list'),
]