from django.urls import path, include
from products.views import index

urlpatterns = [
    path('cat/', index, name=''),


]