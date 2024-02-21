from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.views import View

from apps.products.models import (
    Category, Product, Ingredient, Tag
)


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


class ProductCategoryPage(View):
    template = 'products/pages/product_category.html'
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
        ).filter(in_stock=True)
    )

    def get_queryset(self, slug: str):
        return self.queryset.filter(category__slug=slug)

    def get(self, request: HttpRequest, category_slug: str) -> HttpResponse:
        category = get_object_or_404(Category, slug=category_slug)
        ingredient_slug = request.GET.get('ingredient')
        tag_slug = request.GET.get('tag')
        queryset = self.get_queryset(category_slug)
        if ingredient_slug:
            queryset = queryset.filter(
                product_ingredients__ingredient__slug=ingredient_slug
            )
        if tag_slug:
            queryset = queryset.filter(
                product_tags__tag__slug=tag_slug
            )
        return render(
            request,
            self.template,
            context={
                'title': category.name,
                'sitemap_links': [
                    {'link': reverse('products:home'), 'name': 'Главная'},
                    {
                        'link': category.get_category_page_url(),
                        'name': category.name
                    },
                ],
                'product_categories': Category.objects.all(),
                'ingredients': Ingredient.objects.all(),
                'tags': Tag.objects.all(),
                'category_products': queryset,
                'current_category': category,
                'active_ingredient_slug': ingredient_slug,
                'active_tag_slug': tag_slug
            }
        )
