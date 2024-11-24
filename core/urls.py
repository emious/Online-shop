
from django.urls import path
from core.views import index


urlpatterns = [
    path('', index, name='home'),
    #path('register/', views.register_view, name='register'),
    #path('profile/', views.profile_view, name='profile'),
]