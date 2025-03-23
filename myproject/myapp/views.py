from django.shortcuts import render, redirect
from django.contrib.auth.models import User  # Keep only this import for User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# ✅ Home View
def home(request):
    return render(request, 'myapp/home.html')

# ✅ Signup View
def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        # Create user with hashed password
        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()

        return redirect('login')  # Redirect to login page

    return render(request, 'myapp/signup.html')  # Render the signup template

# ✅ Login View
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        # Authenticate user
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)  # Log the user in
            return redirect('dashboard')  # Redirect to dashboard
        else:
            messages.error(request, 'Invalid username or password')

    return render(request, 'myapp/login.html')

# ✅ Logout View
def logout_view(request):
    logout(request)
    return redirect('login')  # Redirect to login page after logout

# ✅ Dashboard View (Now Corrected)
@login_required
def dashboard(request):
    return render(request, 'myapp/dashboard.html', {'user': request.user})

# ✅ Profile View
@login_required
def profile(request):
    return render(request, 'myapp/profile.html')  # Fixed template path

# ✅ Settings View
@login_required
def settings(request):
    return render(request, 'myapp/settings.html')  # Fixed template path

# ✅ Reports View
@login_required
def reports(request):
    return render(request, 'myapp/reports.html')  # Fixed template path
