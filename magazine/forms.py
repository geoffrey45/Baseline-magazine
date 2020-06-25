from django import forms
from .views import Article
from django.contrib.auth.models import User
class NewsLetterForm(forms.Form):
    your_name = User.first_name
    email = User.email
    
class NewArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        exclude = ['editor', 'pub_date']
        widgets = {
            'tag': forms.CheckboxSelectMultiple(),
        }