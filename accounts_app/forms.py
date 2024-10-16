# from django.forms import ModelForm
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
# from django.core import validators
from django.core.exceptions import ValidationError


class LoginForm(forms.ModelForm):
    error_css_class = "login-error"
    
    class Meta:
        model = User
        fields = ("username", "password",)

    username = forms.CharField(max_length=250, widget=forms.TextInput, required=False)
    password = forms.CharField(max_length=250, widget=forms.PasswordInput, required=False)

    username.widget.attrs['placeholder'] = 'Username'
    password.widget.attrs['placeholder'] = 'Password'

    def clean_username(self):
        if not self.data['username']:
            self._errors['username'] = 'Username required!'
    def clean_password(self):
        if not self.data['password']:
            self._errors['password'] = 'Password required!'



class UserRegisterForm(UserCreationForm):
    username = forms.CharField(max_length=250, widget=forms.TextInput, error_messages={'required': 'Please enter a unique username'})
    email = forms.EmailField(max_length=250, widget=forms.EmailInput, error_messages={'required': 'Please enter a valid email address'})
    password1 = forms.CharField(max_length=250, widget=forms.PasswordInput)
    password2 = forms.CharField(max_length=250, widget=forms.PasswordInput)

    # setting the placeholder text for each of the fields to provide guidance to the user on what information to enter in each field
    # Meta defines the model that the form is based on (the User model)
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
    # sets custom placeholder text for each of the form fields
    username.widget.attrs['placeholder'] = 'Username'
    email.widget.attrs['placeholder'] = 'Email address'
    password1.widget.attrs['placeholder'] = 'Password'
    password2.widget.attrs['placeholder'] = 'Confirm Password'


    # checking the validity of email addresses (server side validation)
    def clean_email(self):
        if not self.data['email'].endswith('@reachfree.co.uk'):
            raise ValidationError("Only Reach Free School emails are allowed (e.g. user@reachfree.co.uk)!")
        return self.data['email']
















# from django import forms
# from cProfile import label
# from django.contrib.auth.models import User
# from django.contrib.auth.forms import UserCreationForm
# from django.core.exceptions import ValidationError


# # Forms accept input from site visitors, and then process and respond to the input.
# class LoginForm(forms.ModelForm):
#     class Meta:
#         # the user model has several fields, and i chose to use just 2 for my registration form
#         model = User
#         # data that would be expected from the user 
#         fields = ('username', 'password',)

#     # types of input is expected for each field
#     # required=False allows for the browser validation to be skipped, so the server validation can appear first
#     username = forms.CharField(max_length=250, widget=forms.TextInput, required=False)
#     password = forms.CharField(max_length=250, widget=forms.PasswordInput, required=False)

#     username.widget.attrs['placeholder'] = 'Username'
#     password.widget.attrs['placeholder'] = 'Password'

#     # client side validation
#     # if there is no data introduced in the username and password fields then it will show the errors messages
#     def clean_username(self):
#         if not self.data['username']:
#             self._error['username'] = 'Username required!'
#     def clean_password(self):
#         if not self.data['password']:
#             self._error['password'] = 'Password required!'




# class UserRegisterForm(UserCreationForm):
#     # the user model has several fields, and i chose to use 4 for my registration form
#     username = forms.CharField(max_length=250, widget=forms.TextInput, error_messages={'required':'Please enter a unique username!'})
#     email = forms.EmailField(max_length=250, widget=forms.EmailInput, error_messages={'required':'Please enter a valid email address!'})
#     # password1 and 2 are already defined by django
#     password1 = forms.CharField(max_length=250, widget=forms.PasswordInput)
#     password2 = forms.CharField(max_length=250, widget=forms.PasswordInput)

#     # Class Meta is used to modify the state of the fields above
#     class Meta:
#         model = User
#         fields = ['username', 'email', 'password1', 'password2']

#     # give the input fields names, to make the user understand what to enter in each input box
#     username.widget.attrs['placeholder'] = 'Username'
#     email.widget.attrs['placeholder'] = 'Email'
#     password1.widget.attrs['placeholder'] = 'Password'
#     password2.widget.attrs['placeholder'] = 'Confirm password'

#     def clean_email(self):
#         if not self.data['email'].endswith('@reachfree.co.uk'):
#             raise ValidationError("Only Reach Free School emails are allowed (e.g. user@reachfree.co.uk)!")
#         return self.data['email']