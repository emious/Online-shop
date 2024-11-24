from django.urls import path, include
from accounts.views import login_view


urlpatterns = [
    path('login/', login_view, name='login_view'),
    path('', include('allauth.urls'))
    #path('register/', views.register_view, name='register'),
    #path('profile/', views.profile_view, name='profile'),
]