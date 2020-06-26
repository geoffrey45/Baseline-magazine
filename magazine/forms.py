from django import forms
from .views import mode
from django.contrib.auth.models import User  
from django.contrib.auth.forms import UserCreationForm  

class NewArticleForm(forms.ModelForm):
    class Meta:
        model = mode
        exclude = ['editor', 'pub_date']
        widgets = {
            'tag': forms.CheckboxSelectMultiple(),
        }
    
class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30,required=False)
    last_name = forms.CharField(max_length = 24,required=False)
    email = forms.EmailField(max_length = 200,help_text='Required')
    birth_date = forms.DateField(help_text='required. Format: YYYY-MM-DD')

    class Meta:
        model = User
        fields = ('username','first_name','last_name','email','password1','password2')