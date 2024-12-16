from django.db import models
from django.db.models import Model
from accounts.models import CustomUser


class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)
    parent = models.ForeignKey('self', null=True, blank=True, related_name='subcategories', on_delete=models.CASCADE)

    def get_all_subcategories(self):
        subcategories = Category.objects.filter(parent=self)
        all_subcategories = list(subcategories)
        for subcategory in subcategories:
            all_subcategories.extend(subcategory.get_all_subcategories())
        return all_subcategories

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Categories"



class Product(models.Model):
    name = models.CharField(max_length=255)  #
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    discount_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    description = models.TextField(blank=True)
    specifications = models.JSONField(default=dict, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    stock = models.PositiveIntegerField(default=0)


    def __str__(self):
        return self.name

    @property
    def is_on_discount(self):
        return self.discount_price is not None and self.discount_price < self.price

    def get_specifications(self):
        return self.specifications.items()


class Attribute(models.Model):
    name = models.CharField(max_length=255)  # نام ویژگی (مثلاً "رنگ", "سایز")
    applicable_categories = models.ManyToManyField(Category, blank=True, related_name="attributes")  # دسته‌بندی‌های مرتبط

    def __str__(self):
        return self.name

    def is_applicable_to(self, category):
        """بررسی می‌کند آیا ویژگی برای این دسته‌بندی مجاز است یا خیر"""
        return self.applicable_categories.filter(id=category.id).exists()





class AttributeValue(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='attributes')  # محصول
    attribute = models.ForeignKey(Attribute, on_delete=models.CASCADE)  # ویژگی
    value = models.CharField(max_length=255)  # مقدار ویژگی (مثلاً "قرمز", "XL")

    def __str__(self):
        return f"{self.attribute.name}: {self.value}"


class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='product_images/')
    is_main = models.BooleanField(default=False)

    def __str__(self):
        return f"Image for {self.product.name}"


class ProductReview(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    rating = models.PositiveSmallIntegerField(choices=[(i, str(i)) for i in range(1, 6)])
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    helpful_votes = models.PositiveIntegerField(default=0)
    unhelpful_votes = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"Review by {self.user.username} for {self.product.name}"

    @property
    def vote_score(self):
        """ (helpful - unhelpful)"""
        return self.helpful_votes - self.unhelpful_votes