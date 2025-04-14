from django.shortcuts import render, redirect
from django.contrib.auth.models import User  # Keep only this import for User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import CommunityPost
from . import views
from django.core.paginator import Paginator
# ✅ Home View



def home(request):
    if request.method == 'POST':
        content = request.POST.get('content')
        image = request.FILES.get('image')
        username = request.user.username if request.user.is_authenticated else 'Anonymous'
        CommunityPost.objects.create(username=username, content=content, image=image)
        return redirect('home')

    # Paginate posts (2 per page)
    posts_list = CommunityPost.objects.all().order_by('-timestamp')
    paginator = Paginator(posts_list, 2)  # Change '2' to how many posts per page you want
    page_number = request.GET.get('page')
    posts = paginator.get_page(page_number)

    return render(request, 'myapp/home.html', {'posts': posts})


# ✅ Signup View
def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        User.objects.create_user(username=username, email=email, password=password)
        return redirect('login')

    return render(request, 'myapp/auth.html', {'mode': 'signup'})


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid username or password')

    return render(request, 'myapp/auth.html', {'mode': 'login'})


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
