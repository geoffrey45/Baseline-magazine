from django import forms
from .views import mode
from django.contrib.auth.models import User    

class NewArticleForm(forms.ModelForm):
    class Meta:
        model = mode
        exclude = ['editor', 'pub_date']
        widgets = {
            'tag': forms.CheckboxSelectMultiple(),
        }

