from django.http import HttpResponse
from django.shortcuts import render, render_to_response

from my_blog.models import Article, Comment


# Create your views here.

def blog(request):
    # 需求1：查询所有博客信息，并返回给前端页面，展示
    blogs = Article.objects.all()

    for blog in blogs:
        # 查询，每篇文章下的所有评论
        comments = blog.comment_set.all()

    """这里的评论跟文章有对应关系，但是不知道如何跟前端交互"""
    """有获取到评论数据，但是return之后，页面并未显示"""

    return render_to_response('blog.html', {'blogs': blogs}, {'comments': comments})


def post_comment(request, id, comment):
    # 需求2：用户提交评论，添加进入数据库

    blog = Article.objects.get(id=id)  # 获取评论的对应博客

    comment = Comment.objects.create(comment=comment, article_id=blog.id)  # 向tb_comment表中添加信息

    return HttpResponse('<h1>添加评论</h1>')
