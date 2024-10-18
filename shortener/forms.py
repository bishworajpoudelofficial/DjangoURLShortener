from django import forms 
from .models import MyURL

class URLForm(forms.ModelForm):
    class Meta:
        model = MyURL
        fields = ['original_url']