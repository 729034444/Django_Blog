from django.db import models


# Create your models here.
class Article(models.Model):
    """文章模型类"""
    title = models.CharField(max_length=50, verbose_name='文章标题')
    content = models.TextField(verbose_name='博客正文')

    class Meta:
        db_table = 'tb_articles'
        verbose_name = '文章和评论'


# 这里还要单独创建一个评论表，评论跟文章是多对1关系
class Comment(models.Model):
    """评论表"""
    comment = models.CharField('评论内容', max_length=240)

    article = models.ForeignKey(Article, on_delete=models.SET_NULL,
                                null=True, verbose_name='文章')

    class Meta:
        db_table = 'tb_comment'
        verbose_name = '评论'


