from django.shortcuts import render, redirect, HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.urls import reverse
from django.contrib.auth import authenticate, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import logout, login, authenticate
from allauth.account.forms import ChangePasswordForm, SignupForm, LoginForm
from .forms import CustomSignupForm, LoginForm, ChangePasswordForm, UpdateProfileForm, MyCustomLoginForm


def view_login(request):
    if request.method == 'POST':
        form = MyCustomLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                # Inject the authenticated user into the request.user property
                login(request, user)
                messages.success(request, 'logged in successfully')
                return redirect('/')
            else:
                pass
    else:
        form = MyCustomLoginForm()
    return render(request, 'account/login.html', {'form': form})


def index(request):
    return render(request, 'index.html')


def signup(request):
    if request.method == 'POST':
        form = CustomSignupForm(request.POST)
        if form.is_valid():
            # import pdb;pdb.set_trace()
            form.save(request)
            return redirect('/')
    else:
        # import pdb;pdb.set_trace()
        form = CustomSignupForm()
    return render(request, 'account/signup.html', {'form': form})


def view_logout(request):
    logout(request)
    return HttpResponseRedirect('/')

# def change_password(request):
#   user = request.user
#   if request.method == 'POST':
#     old_password = request.POST.get('old_password')
#     new_password = request.POST.get('new_password')
#     # Check if the old password is correct
#     if user.check_password(old_password):
#     # change Password
#       user.set_password(new_password)
#       user.save()
#       return HttpResponse('password has been updated')
#     else:
#       return HttpResponse('Original password error')
#   return render(request, 'change_password.html')


def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Your password was successfully updated!')
            return redirect('change_password')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'account/change_password.html', {'form': form})


def update_profile(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = UpdateProfileForm(request.POST, instance=request.user)
            if form.is_valid():
                form.save()
        else:
            form = UpdateProfileForm(instance=request.user)
        return render(request, 'account/profile_update.html', {'form': form})
    else:
        return render(request, 'account/login.html')
