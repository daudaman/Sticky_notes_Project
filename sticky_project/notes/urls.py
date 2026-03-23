# URL routing ko import karo
from django.urls import path
# Is app ke views ko import karo
from . import views

# App ke sab URL patterns (routes)
urlpatterns = [
    # Home page - sab notes dikhao
    path('', views.note_list, name='note_list'),
    # Naya note create karne ka page
    path('new/', views.note_create, name='note_create'),
    # Kisi note ko edit karne ka page (pk = note ki ID)
    path('<int:pk>/edit/', views.note_edit, name='note_edit'),
    # Note ko delete karne ka page
    path('<int:pk>/delete/', views.note_delete, name='note_delete'),
]
