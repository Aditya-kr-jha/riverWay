from django.shortcuts import render
from django.shortcuts import get_object_or_404

from store.models import Category, Product

# Create your views here.


def store(request):
    all_products = Product.objects.all()
    context = {"all_products": all_products}
    return render(request, "store/store.html", context)


def categories(request):
    all_categories = Category.objects.all()
    return {"all_categories": all_categories}


def category_list(request, category_slug=None):
    category = get_object_or_404(Category, slug=category_slug)
    products = Product.objects.filter(category=category)
    context = {"products": products, "category": category}
    return render(request, "store/category_list.html", context)


def product_info(request, slug):
    product = get_object_or_404(Product, slug=slug)
    context = {"product": product}
    return render(request, "store/product_info.html", context)
