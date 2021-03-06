from django.conf.urls import url, include

from blog import views

urlpatterns = [
    url(r'^heatmap$', views.heatmap, name='heatmap'),
    url(r'^usermap$', views.usermap, name='usermap'),
    url(r'^current_user$', views.current_user, name='current_user'),
    url(r'^$', views.posts_list, name='posts_list'),
    url(r'^post/(?P<pk>\d+)/$', views.posts_detail, name='posts_detail'),
    url(r'^post/write$', views.writePost, name='writePost'),
    url(r'^post/(?P<pk>\d+)/edit/$', views.editPost, name='editPost'),
    url(r'^sendmsg$', views.sendmsg, name='sendmsg'),
    url(r'^success$', views.success, name='success'),
    url(r'^failure$', views.failure, name='failure'),
    url(r'^ner$', views.ner, name='ner'),
    url(r'^ner/process$', views.ner_process, name='ner_process'),
    url(r'^sentiment$', views.sentiment, name="sentiment"),
    url(r'^sentiment/process$', views.sentiment_process, name="sentiment_process"),
    url(r'^activity$', views.get_activity, name="activity"),
    url(r'^property$', views.get_property, name="property"),
    url(r'^profile/query$',views.profile_query,name='profile_query'),
    url(r'^query/process$',views.query_process,name='query_process'),
    url(r'^test$', views.test, name='test'),
    url(r'^test/process$', views.test_process, name='test_process'),
    url(r'^froala_editor/', include('froala_editor.urls')),
    # url(r'^usermap',views.posts_list,name='posts_list'),
]
