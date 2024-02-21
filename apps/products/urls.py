from django.urls import path

from apps.products.views import ProductsMainPage, ProductCategoryPage

app_name = 'products'
urlpatterns = [
    path('', ProductsMainPage.as_view(), name='home'),
    path('home', ProductsMainPage.as_view(), name='home_2'),
    path(
        'products/<slug:category_slug>',
        ProductCategoryPage.as_view(),
        name='category_products'
    ),
]
