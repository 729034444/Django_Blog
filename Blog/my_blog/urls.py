from django.urls import re_path
from my_blog import views

urlpatterns = [
    re_path(r'^blog/$', views.blog),
    re_path(r'^post_comment/$', views.post_comment)
]
