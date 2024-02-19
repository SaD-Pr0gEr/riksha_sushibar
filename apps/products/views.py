from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.utils.translation import gettext_lazy as _
from django.views import View

from apps.products.models import Category, Product


class ProductsMainPage(View):
    queryset = (
        Product.objects
        .select_related('category')
        .prefetch_related(
            'product_ingredients', 'product_tags',
            'product_attributes'
        )
        .prefetch_related(
            'product_ingredients__ingredient', 'product_tags__tag',
            'product_attributes__attribute'
        )
    )
    template = 'products/pages/index.html'

    def get(self, request: HttpRequest) -> HttpResponse:
        return render(
            request,
            self.template,
            context={
                'title': _('Products'),
                'product_categories': Category.objects.all(),
                'new_products': self.queryset.filter(
                    in_stock=True, new_product=True
                ).all()
            }
        )
