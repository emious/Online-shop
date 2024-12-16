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

def product_list_view(request,  category_slug):
    # گرفتن دسته‌بندی با استفاده از اسلاگ
    category = get_object_or_404(Category, slug=category_slug)

    # دریافت تمام زیرمجموعه‌ها (مستقیم و غیرمستقیم)
    subcategories = category.get_all_subcategories()

    # اضافه کردن خود دسته‌بندی به لیست زیرمجموعه‌ها
    subcategories.append(category)

    # فیلتر کردن محصولات با توجه به دسته‌بندی و زیرمجموعه‌ها
    products = Product.objects.filter(category__in=subcategories)


    return render(request, 'products/category-market.html', {
        'category': category,
        'subcategories': subcategories,
        'products': products,})

