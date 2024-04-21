# myapp/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm

class SignupForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Required. Enter a valid email address.')

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']



class UserLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

# forms.py
class JobPositionForm(forms.Form):
    title = forms.CharField(max_length=100)
    description = forms.CharField(widget=forms.Textarea)
    requirements = forms.CharField(widget=forms.Textarea)
    pay_range = forms.ChoiceField(choices=(
        ('0-1000', '$0 - $1000'),
        ('1000-2000', '$1000 - $2000'),
        ('2000-3000', '$2000 - $3000'),
        ('3000-4000', '$3000 - $4000'),
    ))
    project_type = forms.ChoiceField(choices=(('single', 'Single Project'), ('group', 'Group Project')), widget=forms.RadioSelect)


class ApplyForm(forms.Form):
    job_title = forms.CharField(max_length=100)
    job_description = forms.CharField(widget=forms.Textarea)
    pay_range = forms.ChoiceField(choices=[('100-200', '100-200'), ('200-300', '200-300'), ('300-400', '300-400')], required=False)
    cv_upload = forms.FileField()

class ProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']
