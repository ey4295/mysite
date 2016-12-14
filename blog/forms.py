from django import forms
from froala_editor.widgets import FroalaEditor

from blog.models import Post


class PostForm(forms.ModelForm):
    #author = forms.CharField(widget=FroalaEditor)
    #title = forms.CharField(widget=FroalaEditor)
    #introduction = forms.CharField(widget=FroalaEditor)
    #content = forms.CharField(widget=FroalaEditor)

    class Meta:
        model=Post
        fields=('author','title','introduction','content',)