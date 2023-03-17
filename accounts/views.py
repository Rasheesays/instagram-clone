from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from .forms import UserLoginForm, SignUpForm, EditProfileForm
from .models import User
# from users.models import Posts, Friends

class UserLogin(LoginView):
    authentication_form = UserLoginForm
    template_name = 'accounts/login.html'

def signup_view(request):
    form = SignUpForm()
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            
            messages.success(request, 'Account created successfully!')
            return redirect('user_profile')

    context = {'SignUpForm': form}
    return render(request, 'accounts/signup.html', context)

@login_required(login_url='user_login')
@user_passes_test(lambda user: user.is_staff is False)
def edit_profile_view(request):
    form = EditProfileForm(instance=request.user)
    if request.method == 'POST':
        form = EditProfileForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            messages.info(request, 'Profile updated successfully!')
            return redirect('user_profile')

    context = {'edit_form': form}
    return render(request, 'accounts/edit-profile.html', context)

@login_required(login_url='user_login')
@user_passes_test(lambda user: user.is_staff is False)
def profile_view(request):
    user_posts = Posts.objects.filter(user=request.user).all()

    context = {
        'my_posts': user_posts, 'total_posts': user_posts.count(),
        'followers': Friends.objects.filter(followed=request.user.userprofile).count(),
        'following': Friends.objects.filter(following=request.user.userprofile).count(),

    }
    return render(request, 'accounts/profile.html', context)


class LogoutUser(LogoutView):
    template_name = 'accounts/logout.html'
