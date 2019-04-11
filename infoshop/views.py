from django.shortcuts import render, get_object_or_404, render_to_response
from .models import Category, Product
from cart.forms import CartAddProductForm


# Страница с товарами
def ProductList(request, category_alias=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_alias:
        category = get_object_or_404(Category, alias=category_alias)
        products = products.filter(category=category)
    return render(request, 'infoshop/product/list.html', {
        'category': category,
        'categories': categories,
        'products': products
    })

# Страница товара
def ProductDetail(request, id, alias):
    product = get_object_or_404(Product, id=id, alias=alias, available=True)
    cart_product_form = CartAddProductForm()
    return render(request, 'infoshop/product/detail.html',
                             {'product': product,
                              'cart_product_form': cart_product_form})
