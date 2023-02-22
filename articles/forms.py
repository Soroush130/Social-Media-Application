from django import forms
from .models import Article


class NewArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        exclude = (
            'user',
            'created',
            'updated',
            'like',
            'count_like'
        )
