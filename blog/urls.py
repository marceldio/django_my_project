from django.urls import path
from blog.apps import BlogConfig
from blog.views import BlogCreateView

app_name = BlogConfig.name

# urlpatterns = [
#     path('', ProductListView.as_view(), name='product_list'),
#
#     path('catalog/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
#     path('create/', ProductCreateView.as_view(), name='product_create'),
#
#     path('contacts', contact, name='contacts'),
# ]

urlpatterns = [
    path('create/', BlogCreateView.as_view(), name='blog_create'),
    # path('', BlogListView.as_view(), name='blog_list'),
    # path('view/<int:pk>/', BlogDetailView.as_view(), name='blog_detail'),
    # path('edit/<int:pk>/', BlogUpdateView.as_view(), name='blog_edit'),
    # path('delete/<int:pk>/', BlogDeleteView.as_view(), name='blog_delete'),
]
