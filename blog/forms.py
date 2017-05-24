from django import forms
from froala_editor.widgets import FroalaEditor

from blog.models import Post, Message


class PostForm(forms.ModelForm):
    # author = forms.CharField(widget=FroalaEditor)
    # title = forms.CharField(widget=FroalaEditor)
    # introduction = forms.CharField(widget=FroalaEditor)
    # content = forms.CharField(widget=FroalaEditor)

    class Meta:
        model = Post
        fields = ('author', 'title', 'introduction', 'content',)


class SendMessage(forms.ModelForm):
    class Meta:
        model = Message
        fields = ('content', 'to_cell')


class NerForm(forms.ModelForm):
    class Meta:
        fields=('document',)

