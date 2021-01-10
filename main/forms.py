from django.contrib.auth.forms import (
    AuthenticationForm, UserCreationForm, PasswordChangeForm
)
from django import forms
from .models import (
    User,
    category1s,
    category2s
)

form_input_base_class = 'p-2 form-input block border w-full mb-2'

class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)

    username = forms.CharField(
        widget = forms.TextInput(
            attrs = {
                'class': form_input_base_class,
            }
        )
    )
    password = forms.CharField(
        widget = forms.PasswordInput(
            attrs = {
                'class': form_input_base_class,
            }
    )
)

class SignUpForm(UserCreationForm):
    required_css_class = 'required'
    class Meta:
        model = User
        fields = [
            'email',
            'company_name',
            'company_name_furigana',
            'thumbnail', 
            'category1', 
            'category2',
            'short_description',
            'description',
            'phone',
            'short_delivery',
            'representative_name',
            'established_at',
            'major_clients',
            'major_products',
            'major_technologies',
            'major_facilities',
            'appeal_points',
            'poc_name',
            'website',
            'password1', 
            'password2', 
        ]
    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = form_input_base_class

class ProfileForm(forms.ModelForm):
    required_css_class = 'required'
    class Meta:
        model = User
        fields = (
            'company_name', 
            'company_name_furigana',
            'thumbnail',
            'category1', 
            'category2',
            'short_description',
            'description',
            'phone',
            'short_delivery',
            'representative_name',
            'established_at',
            'major_clients',
            'major_products',
            'major_technologies',
            'major_facilities',
            'appeal_points',
            'poc_name',
            'website',
        )
        
    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            if visible.field.required:
                visible.field.label = f'{visible.field.label}*'
            visible.field.widget.attrs['class'] = form_input_base_class

class PasswordForm(PasswordChangeForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = form_input_base_class
