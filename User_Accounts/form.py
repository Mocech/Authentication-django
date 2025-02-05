from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'id': 'username'})
        self.fields['password1'].widget.attrs.update({'id': 'password1'})
        self.fields['password2'].widget.attrs.update({'id': 'password2'})
        self.fields['email'].widget.attrs.update({'id': 'email'})

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email']
        
class ProfileUpdateForm(forms.ModelForm):
    
    class Meta:
        model = Profile
        fields = ['image']       
        
# def __init__(self,*args,**kwargs):
#     super(ProfileUpdateForm,self).__init__(*args,**kwargs)
#     self.fields['image'].required = False 
        
        
        
        
        
        