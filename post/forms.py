from django import forms
from .models import Post,Contact

class PostForm(forms.ModelForm):
    class Meta:
        model=Post
        fields=[
            'title','body','slug','image'
        ]

class ContactForm(forms.ModelForm):
    class Meta:
        model=Contact
        fields= '__all__'