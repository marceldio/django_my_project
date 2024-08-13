from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from pytils.translit import slugify

from catalog.models import Product


class ProductCreateView(CreateView):
    model = Product
    fields = ("product", "description", "slug", "image", "category", "price", "is_published")
    template_name = ('main/product_form.html')
    success_url = reverse_lazy('catalog:product_list')

    def form_valid(self, form):
        if form.is_valid():
            new_product = form.save()
            new_product.slug = slugify(new_product.product)
            new_product.save()
        return super().form_valid(form)
    # def contact(request):
    #     if request.method == 'POST':
    #         name = request.POST.get('name')
    #         tel = request.POST.get('tel')
    #         message = request.POST.get('message')
    #         print(f'You have new message from {name}({tel}): {message}')
    #     return render(request, 'main/contact.html')

class ProductListView(ListView):
    model = Product
    template_name = ('main/product_list.html')

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset()
        queryset = queryset.filter(is_published=True)
        return queryset


class ProductDetailView(DetailView):
    model = Product
    template_name = ('main/product_detail.html')

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.view_counter += 1
        self.object.save(update_fields=['view_counter'])  # Only update view_counter field
        return self.object


class ProductUpdateView(UpdateView):
    model = Product
    fields = ("product", "description", "slug", "image", "category", "price", "is_published")
    template_name = ('main/product_form.html')

    def form_valid(self, form):
        if form.is_valid():
            new_product = form.save()
            new_product.slug = slugify(new_product.product)
            new_product.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('catalog:product_view', args=[self.kwargs.get('pk')])


class ProductDeleteView(DeleteView):
    model = Product
    template_name = ('main/product_delete.html')
    success_url = reverse_lazy('catalog:product_list')
