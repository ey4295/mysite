from django.contrib import admin

# Register your models here.
from blog.models import Post, User_Request

admin.site.register(Post)
admin.site.register(User_Request)