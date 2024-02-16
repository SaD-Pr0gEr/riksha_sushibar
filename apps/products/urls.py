from django.urls import path

from apps.products.views import ProductsMainPage

app_name = 'products'
urlpatterns = [
    path('', ProductsMainPage.as_view(), name='home'),
    path('home', ProductsMainPage.as_view(), name='home_2'),
]
