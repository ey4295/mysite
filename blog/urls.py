from django.conf.urls import url

from blog import views

urlpatterns=[
    url(r'^$',views.posts_list,name='posts_list'),
    url(r'^post/(?P<pk>\d+)/$',views.posts_detail,name='posts_detail'),
]