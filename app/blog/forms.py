from django import forms
from .models import Post


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text', 'image')


# class PostForm(forms.Form):
#     title = forms.CharField(max_length=200)
#     # text = forms.TextInput()
#     text = forms.CharField(widget=forms.Textarea)
#     # text = forms.T
#     # random = forms.CharField()
#     image = forms.ImageField()

    # class Meta:
    #     model = Post
    #     fields = ('title', 'text', 'image')
