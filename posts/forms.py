from django import forms
from .models import Post


class NewPostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ('user', 'tag', 'like', 'count_like','created')
        # fields = "__all__"

# class NewPostForm(forms.Form):
#     file = forms.ImageField()
#     description = forms.CharField(widget=forms.TextInput)
