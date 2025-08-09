from django.shortcuts import render

from catalog.models import Product


def contacts(request):
    return render(request, 'contacts.html')


def products_list(request):
    products = Product.objects.all()
    context = {"products": products}
    return render(request, 'products_list.html', context)


def product_detail(request, pk):
    product = Product.objects.get(pk=pk)
    context = {"product": product}
    return render(request, 'product_detail.html', context)
