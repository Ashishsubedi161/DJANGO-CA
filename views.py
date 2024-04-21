# myapp/views.py
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import SignupForm, UserLoginForm
from .forms import JobPositionForm, ApplyForm
from .forms import ProfileForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout as auth_logout

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('login')
    else:
        form = SignupForm()
    return render(request, 'signup.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            response = redirect('main_page')
            response.set_cookie('username', user.username) 
            return response
        else:
            return HttpResponse('Invalid username or password.')
    else:
        return render(request, 'login.html')


def main_view(request):
    job_position_form = JobPositionForm(request.POST or None)
    apply_form = ApplyForm(request.POST or None)

    if job_position_form.is_valid():
        # Process job position form submission
        # Save job position to the database
        return redirect('main')  # Redirect to main page after form submission

    if apply_form.is_valid():
        # Process apply form submission
        # Save application to the database
        return redirect('main')  # Redirect to main page after form submission

    return render(request, 'main.html', {'job_position_form': job_position_form, 'apply_form': apply_form})

def logout(request):
    auth_logout(request)
    return redirect('login')

# views.py
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import ProfileForm

@login_required
def profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')  # Redirect to profile page after successful update
    else:
        form = ProfileForm(instance=request.user)

    return render(request, 'profile.html', {'form': form})
