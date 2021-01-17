from django import forms


# 借助forms实现评论功能
class CommentForm(forms.Form):
    comment = forms.CharField(label='发表评论', error_messages={
        'required':'请填写评论内容！',
        'max_length':'评论内容过长。'
    })
