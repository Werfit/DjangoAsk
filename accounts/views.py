from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login
from django.contrib.auth.decorators import login_required

from .forms import SignUpForm, UpdateUserForm, UpdateUserProfileForm


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)

        if form.is_valid():
            user = form.save()

            auth_login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'accounts/signup.html', {'form': form})


@login_required
def update_user(request):
    user = request.user

    if request.method == 'POST':
        form = UpdateUserForm(request.POST, instance=user)
        avatar_form = UpdateUserProfileForm(request.POST, request.FILES, instance=user.profile)

        if form.is_valid() and avatar_form.is_valid():
            form.save()
            avatar_form.save()
    else:
        form = UpdateUserForm(instance=user)
        avatar_form = UpdateUserProfileForm(instance=user.profile)

    return render(request, 'accounts/settings.html', {'form': form, 'extra': avatar_form})

