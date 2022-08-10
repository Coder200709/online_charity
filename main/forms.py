from django import forms


class PostCreateForm(forms.Form):
    title = forms.CharField(widget=forms.TextInput)
    body = forms.CharField(widget=forms.Textarea)
    image = forms.ImageField(widget=forms.FileInput)
