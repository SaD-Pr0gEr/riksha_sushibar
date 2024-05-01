from typing import Any

from django.core.paginator import Paginator
from django.db.models import QuerySet
from django.http import HttpRequest, HttpResponse, Http404
from django.shortcuts import render, get_object_or_404
from django.utils.translation import gettext_lazy as _

from apps.products.models import (
    Category, Product, Ingredient, Tag
)
from apps.views import BasePagesView


class BaseProductsView(BasePagesView):
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


class ProductsMainPage(BaseProductsView):
    page_title = _('Products')
    template = 'products/pages/index.html'

    def get_context_data(self, *args, **kwargs) -> dict:
        return super().get_context_data() | {
            'new_products': self.queryset.filter(
                new_product=True
            )[:5]
        }


class ProductCategoryPage(BaseProductsView):
    template = 'products/pages/product_category.html'

    def get_sitemap_links(self, category: Category) -> list[dict[str, Any]]:
        return super().get_sitemap_links() + [
            {
                'link': category.get_category_page_url(),
                'name': category.name
            },
        ]

    def get_context_data(self, *args, **kwargs) -> dict:
        category: Category = kwargs.get('category')
        products_queryset: QuerySet[Product] = kwargs.get('queryset')
        paginator = Paginator(products_queryset, 6)
        paginator_page = kwargs.get('paginator_page')
        current_page = paginator.get_page(paginator_page)
        context = {
            'title': category.name,
            'sitemap_links': self.get_sitemap_links(category),
            'ingredients': Ingredient.objects.all(),
            'tags': Tag.objects.all(),
            'current_category': category,
            'paginator': paginator,
            'category_products': current_page,
            'current_page': paginator_page,
            'active_tag_slug': kwargs.get('tag_slug'),
            'active_ingredient_slug': kwargs.get('active_ingredient_slug')
        }
        return super().get_context_data() | context

    def get(self, request: HttpRequest, category_slug: str) -> HttpResponse:
        category = get_object_or_404(Category, slug=category_slug)
        self.page_title = category.name
        ingredient_slug: str = self.request.GET.get('ingredient')
        tag_slug: str = self.request.GET.get('tag')
        paginator_page: str | int = self.request.GET.get('page', '1')
        paginator_page = 1 if not paginator_page.isdecimal() else int(paginator_page)
        queryset: QuerySet[Product] = self.filter_queryset(
            category__slug=category.slug,
            product_ingredients__ingredient__slug=ingredient_slug,
            product_tags__tag__slug=tag_slug
        )
        return render(
            request,
            self.template,
            context=self.get_context_data(
                category=category,
                queryset=queryset,
                paginator_page=paginator_page,
                tag_slug=tag_slug,
                active_ingredient_slug=ingredient_slug
            )
        )


class ProductDetailPage(BaseProductsView):
    template = 'products/pages/product_detail.html'

    def get_sitemap_links(self, product: Product) -> list[dict[str, Any]]:
        return super().get_sitemap_links() + [
            {
                'link': product.category.get_category_page_url(),
                'name': product.category.name
            },
            {
                'link': product.get_product_detail_url(),
                'name': product.name
            }
        ]

    def get_context_data(self, product: Product) -> dict:
        context = {
            'title': product.name,
            'sitemap_links': self.get_sitemap_links(product),
            'product': product
        }
        return super().get_context_data() | context

    def get(self, request: HttpRequest, product_slug: str):
        product: Product | None = self.filter_queryset(slug=product_slug).first()
        if not product:
            raise Http404('product not found')
        return render(
            request,
            self.template,
            self.get_context_data(product)
        )
