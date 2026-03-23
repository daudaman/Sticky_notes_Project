# Django admin panel
from django.contrib import admin
# URL routing
from django.urls import path, include
# Built-in Django authentication views (login, logout)
from django.contrib.auth import views as auth_views
# Notes app ke views
from notes import views as note_views

# Puri project ke URL patterns (main routes)
urlpatterns = [
    # Admin panel - database manage karne ke liye
    path('admin/', admin.site.urls),
    # Notes app ke sab URLs (notes/ ke baad)
    path('notes/', include('notes.urls')),
    # New user register karne ka page
    path('register/', note_views.register_view, name='register'),
    # User ko login karne ka page
    path('login/', auth_views.LoginView.as_view(template_name='notes/login.html'), name='login'),
    # User ko logout karne ka page
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    # Home page - login page per redirect karo
    path('', auth_views.LoginView.as_view(template_name='notes/login.html'), name='home'),
]
