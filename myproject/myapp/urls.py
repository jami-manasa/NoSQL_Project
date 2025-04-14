from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('signup/', signup, name='signup'),
    path('login/', login_view, name='login'),
    path('', home, name='home'),
    path('logout/', logout_view, name='logout'),
    path('dashboard/', dashboard, name='dashboard'),
    path('profile/', profile, name='profile'),
    path('settings/', views.settings, name='settings'),
    path('reports/', reports, name='reports'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
