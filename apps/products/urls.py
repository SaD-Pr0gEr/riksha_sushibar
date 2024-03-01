from django.urls import path

from apps.products.views import ProductsMainPage, ProductCategoryPage, ProductDetailPage

app_name = 'products'
urlpatterns = [
    path('', ProductsMainPage.as_view(), name='home'),
    path('home', ProductsMainPage.as_view(), name='home_2'),
    path(
        'products/<slug:category_slug>',
        ProductCategoryPage.as_view(),
        name='category_products'
    ),
    path(
        'products/detail/<slug:product_slug>',
        ProductDetailPage.as_view(),
        name='product_detail'
    ),
]
