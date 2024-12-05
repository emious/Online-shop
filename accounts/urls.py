from django.urls import path, include
from accounts.views import auth_view, dashboard_view


urlpatterns = [
    path('auth/', auth_view, name='auth_view'),
    path('dashboard/', dashboard_view, name='dashboard_view'),
    path('', include('allauth.urls'))

]