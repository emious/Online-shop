from itertools import product

from django.shortcuts import render, get_object_or_404

from products.models import Product, ProductImage, Category

def product_detail_view(request, product_id):
    single_product = get_object_or_404(Product, id=product_id)
    main_image = single_product.images.filter(is_main=True).first()
    return render(request, 'products/product-sidebar.html',
                  {'product': single_product,
                          'main_image': main_image,})

def product_category(request):
    return render(request, 'products/category-market.html')