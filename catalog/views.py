from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, TemplateView, CreateView, UpdateView, DeleteView

from catalog.forms import ProductForm
from catalog.models import Product, Category
from catalog.services import get_products_from_cache


class ContactsView(TemplateView):
    template_name = 'catalog/contacts.html'


class ProductListView(ListView):
    model = Product
    template_name = 'catalog/product_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context

    def get_queryset(self):
        return get_products_from_cache()


class ProductDetailView(LoginRequiredMixin, DetailView):
    model = Product


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'catalog/product_form.html'
    success_url = reverse_lazy('catalog:products_list')
    login_url = reverse_lazy('users:login')


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'catalog/product_form.html'
    success_url = reverse_lazy('catalog:products_list')
    login_url = reverse_lazy('users:login')


class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    success_url = reverse_lazy('catalog:products_list')
    login_url = reverse_lazy('users:login')


def category_products(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    products = Product.objects.filter(category=category)

    all_categories = Category.objects.all()

    context = {
        'category': category,  # текущая категория
        'categories': all_categories,  # все категории для меню
        'products': products  # продукты текущей категории
    }
    return render(request, 'catalog/category_products.html', context)
