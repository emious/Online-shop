from itertools import product
from lib2to3.fixes.fix_input import context

from django.shortcuts import render, get_object_or_404

from products.models import Product, ProductImage, Category

def product_detail_view(request, product_id):
    single_product = get_object_or_404(Product, id=product_id)
    main_image = single_product.images.filter(is_main=True).first()
    return render(request, 'products/product-sidebar.html',
                  {'product': single_product,
                          'main_image': main_image,})

def product_list_view(request,  category_id):
    cat_list = Category.objects.filter(parent_id=category_id)
    return render(request, 'products/category-market.html', {"cat_list": cat_list})