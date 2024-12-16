from django.urls import path, include
from products.views import product_detail_view, product_list_view

urlpatterns = [
    path('detail/<int:product_id>/', product_detail_view, name='product_detail_view'),
    path('list/<slug:category_slug>/', product_list_view, name='product_list_view'),

]