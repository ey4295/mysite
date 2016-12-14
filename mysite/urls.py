from django.contrib.auth.views import login
from django.contrib import auth
from django.conf.urls import include, url
from django.contrib import admin
#/home/xuqh/anaconda2/lib/python2.7/site-packages/django
urlpatterns = [
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/login/$', auth.views.login, name='login'),
    url(r'^accounts/logout/$', auth.views.logout, name='logout', kwargs={'next_page': '/'}),
    url(r'',include('blog.urls')),
]
