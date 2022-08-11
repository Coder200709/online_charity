from django import forms
from .models import PostModel


class PostCreateForm(forms.Form):
    title = forms.CharField(widget=forms.TextInput)
    body = forms.CharField(widget=forms.Textarea)
    image = forms.ImageField(widget=forms.FileInput)


class PostUpdateForm(forms.ModelForm):
    class Meta:
        model = PostModel
        fields = ['title', 'body', 'image']
