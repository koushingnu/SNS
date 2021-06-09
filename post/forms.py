from django import forms


class PostForm(forms.Form):
    content = forms.CharField(max_length=5000,
                             widget=forms.Textarea(attrs={'class': 'form-contorol'}))
