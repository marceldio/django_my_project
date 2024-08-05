from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView

from catalog.models import Product


class ProductListView(ListView):
    model = Product
    template_name = ('main/product_list.html')


class ProductDetailView(DetailView):
    model = Product
    template_name = ('main/product_detail.html')


class ProductCreateView(CreateView):
    model = Product
    fields = ("product", "description", "image", "category", "price")
    success_url = reverse_lazy('catalog:product_list')


def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        tel = request.POST.get('tel')
        message = request.POST.get('message')
        print(f'You have new message from {name}({tel}): {message}')
    return render(request, 'main/contact.html')

