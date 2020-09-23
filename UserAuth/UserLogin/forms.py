from django.contrib.auth.models import User
from django import forms
from allauth.account.forms import ChangePasswordForm, SignupForm, LoginForm
from django.contrib.auth.forms import UserChangeForm


class CustomSignupForm(SignupForm):

    class Meta:
        fields = '__all__'

    def save(self, request):
        user = super(CustomSignupForm, self).save(request)
        # user.username = self.cleaned_data['username']
        # user.password2 = self.cleaned_data['password2']
        user.save()
        return user

    def clean(self):
        super(CustomSignupForm, self).clean()
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')
        if password and password != confirm_password:
            self._errors['password'] = self.error_class(['Passwords don\'t match'])
        return self.cleaned_data


class MyCustomLoginForm(LoginForm):

    username = forms.CharField(max_length = 100)
    password = forms.CharField(max_length=32, widget=forms.PasswordInput)

    def login(self, *args, **kwargs):
        # Add your own processing here.
        # You must return the original result.
        return super(MyCustomLoginForm, self).login(*args, **kwargs)

# class MyCustomChangePasswordForm(ChangePasswordForm):
#     def save(self):
#       # Ensure you call the parent class's save.
#       # .save() does not return anything
#       super(MyCustomChangePasswordForm, self).save()
#       # user.password = self.cleaned_data['password']
#       # Add your own processing here.


class UpdateProfileForm(UserChangeForm):
    password = None

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']
