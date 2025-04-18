from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.login_view, name='login'),
    path('', views.home, name='home'),
    path('logout/', views.logout_view, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('profile/', views.profile, name='profile'),
    path('settings/', views.settings, name='settings'), 
    path('reports/', views.reports, name='reports'),
    path('mentorship/posts/', views.mentorship_posts, name='mentorship_posts'),  
    path('mentorship/request/', views.send_request, name='send_request'),

    path('mentorship/create/', views.create_mentorship_post, name='create_mentorship_post'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
