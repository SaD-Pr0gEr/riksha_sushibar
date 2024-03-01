from typing import Any

from django.db.models import QuerySet
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse
from django.views import View

from apps.products.models import Category


class BasePagesView(View):
    page_title: str | None = None
    template: str | None = None
    queryset: QuerySet | None = None

    def get_queryset(self, *args, **kwargs) -> QuerySet:
        raise NotImplemented

    def filter_queryset(self, **filter_fields) -> QuerySet:
        if not self.queryset:
            raise NotImplemented
        filter_ready = {key: value for key, value in filter_fields.items() if value}
        self.queryset = self.queryset.filter(**filter_ready)
        return self.queryset

    def get_sitemap_links(self, *args, **kwargs) -> list[dict[str, Any]]:
        return [
            {'link': reverse('products:home'), 'name': 'Главная'},
        ]

    def get_context_data(self, *args, **kwargs) -> dict:
        return {
            'product_categories': Category.objects.all(),
            'title': self.page_title
        }

    def get(self, *args, **kwargs) -> HttpResponse:
        if not self.template:
            raise NotImplemented
        return render(
            self.request,
            self.template,
            context=self.get_context_data()
        )
