from django import forms
from .models import Comment

class CommentForm(forms.Form):
    body = forms.CharField(max_length=256)
    body.widget.attrs.update({'class': 'message_input'})
    def save(self):
        new_comment = Comment.objects.create(
            body=self.cleaned_data['body']
        )
        return new_comment