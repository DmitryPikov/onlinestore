from django.views.generic import ListView, DetailView, TemplateView

from catalog.models import Product


class ContactsView(TemplateView):
    template_name = 'catalog/contacts.html'


class ProductListView(ListView):
    model = Product


class ProductDetailView(DetailView):
    model = Product
