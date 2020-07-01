from django import forms
from .views import mode
from .models import Profile,Comment
from django.contrib.auth.models import User 
from django.contrib.auth.forms import UserCreationForm 
from tinymce.models import HTMLField

class NewArticleForm(forms.ModelForm):
    class Meta:
        model = mode
        exclude = ['editor', 'created_on','slug']
        widgets = {
            'tag': forms.CheckboxSelectMultiple(),
        }
        
class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2',)    
         
class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField(max_length=200)

    class Meta:
        model = User
        fields = ['username','email']

class ProfileUpdateForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ['image','location','birth_date','bio']
        
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name','email','body')
        
