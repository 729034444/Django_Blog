from django.urls import re_path
from my_blog import views

urlpatterns = [
    re_path(r'^$', views.blog),
    re_path(r'^blog/$', views.blog),
    re_path(r'^get_details/(\d+)/$', views.get_details, name='blog_get_detail')
]
