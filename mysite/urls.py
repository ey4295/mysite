from django.conf.urls import include, url
from django.contrib import admin
#/home/xuqh/anaconda2/lib/python2.7/site-packages/django
urlpatterns = [
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'',include('blog.urls')),
]
