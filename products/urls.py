from django.urls import path, include
from products.views import product_detail_view, product_category

urlpatterns = [
    path('detail/<int:product_id>/', product_detail_view, name='product_detail_view'),
    path('product_category/', product_category, name='product_category'),

]