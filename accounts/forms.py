from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser
from allauth.account.forms import SignupForm
from allauth.account.forms import ChangePasswordForm
from django import forms

class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = ('email',)

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('email',)
    
class CustomSignUpForm(SignupForm):
    first_name = forms.CharField(max_length=30, label='Vorname')
    last_name = forms.CharField(max_length=30, label='Nachname')
    
    class Meta:
        model = CustomUser
        fields = ('email', 'first_name', 'last_name')


    def save(self, request):
        user = super(CustomSignUpForm, self).save(request)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.save()
        return user
