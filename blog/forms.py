from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['body']
    
    body = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control custom-text', 'col': 40, 'rows': 4}))
