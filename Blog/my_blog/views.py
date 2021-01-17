from django.http import HttpResponse, Http404
from django.shortcuts import render, render_to_response

from my_blog.models import Article, Comment
from my_blog.forms import CommentForm


# Create your views here.

def blog(request):
    # 需求1：查询所有博客信息，并返回给前端页面，展示
    blogs = Article.objects.all()

    return render_to_response('blog.html', {'blogs': blogs})


"""
之前想把评论在首页跟随博客显示，但是仔细思考过感觉不应该这样：
如果一个文章评论太多，会直接把其他所有文章挤下去。

所以，这里做了一个调整：首页不显示评论，点击文章进入详情时，显示评论，且可以发表评论。
"""


def get_details(request, blog_id):
    # 需求2：点击文章链接，进入文章详细信息；在这里展示评论列表和发表评论

    try:
        blog = Article.objects.get(id=blog_id)
    except Article.DoesNotExist:
        raise Http404

    if request.method == 'GET':
        # GET请求获取文章所有评论
        form = CommentForm()
    else:
        # POST请求提交评论
        form = CommentForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            Comment.objects.create(comment=data.get('comment'), article_id=blog_id)

    comment_data = {
        'blog': blog,
        'comments': blog.comment_set.all(),
        'form': form
    }

    return render(request, 'blog_details.html', comment_data)
