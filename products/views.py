from itertools import product
from lib2to3.fixes.fix_input import context
from products.form import ProductReviewForm
from django.shortcuts import render, get_object_or_404, redirect
from products.models import Product, ProductReview, Category
from django.db.models import QuerySet

def product_detail_view(request, product_id):
    single_product = get_object_or_404(Product, id=product_id)
    main_image = single_product.images.filter(is_main=True).first()
    related_products = single_product.get_related_products().prefetch_related('images')[:5]
    reviews = ProductReview.objects.filter(product=single_product).order_by('-created_at')
    random_products = Product.objects.filter(category_id=single_product.category).order_by("?")[:4]

    review_form = None
    if request.user.is_authenticated:
        if request.method == 'POST':
            review_form = ProductReviewForm(request.POST)
            if review_form.is_valid():
                review = review_form.save(commit=False)
                review.product = single_product
                review.user = request.user
                review.save()

                return redirect('product_detail_view', product_id=single_product.id)
        else:
            review_form = ProductReviewForm()


    return render(request, 'products/product-sidebar.html',
                  {'product': single_product,
                  'related_products': related_products,
                  'main_image': main_image,
                   'reviews': reviews,
                   'review_form': review_form,
                   'random_products':random_products,
                   })

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

