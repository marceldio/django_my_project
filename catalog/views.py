from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from catalog.models import Product


class ProductListView(ListView):
    model = Product
    template_name = ('main/product_list.html')
    # app.name/<model_name>_<action
    # catalog/product_list.html

# def products_list(requests):
#     products = Product.objects.all()
#     context = {'products': products}
#     return render(requests, 'main/products_list.html', context)


class ProductDetailView(DetailView):
    model = Product
    template_name = ('main/product_detail.html')
    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.view_counter += 1
        self.object.save()
        return self.object

# def card(request, pk):
#     product = get_object_or_404(Product, pk=pk)
#     context = {'product': product}
#     return render(request, 'main/product_detail.html', context)


class ProductCreateView(CreateView):
    model = Product
    fields = ("product", "description", "image", "category", "price")
    template_name = ('main/product_form.html')
    success_url = reverse_lazy('catalog:product_list')


class ProductUpdateView(UpdateView):
    model = Product
    fields = ("product", "description", "image", "category", "price")
    template_name = ('main/product_form.html')
    success_url = reverse_lazy('catalog:product_list')

    def get_success_url(self):
        return reverse('catalog:product_detail', args=[self.kwargs.get('pk')])


class ProductDeleteView(DeleteView):
    model = Product
    template_name = ('main/product_confirm_delete.html')
    success_url = reverse_lazy('catalog:product_list')


def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        tel = request.POST.get('tel')
        message = request.POST.get('message')
        print(f'You have new message from {name}({tel}): {message}')
    return render(request, 'main/contact.html')

