from django.contrib import admin
from django.contrib.admin import ModelAdmin

from apps.products.models import (
    Category, Ingredient, Tag, Attribute, Product,
    ProductIngredient, ProductTag, ProductAttribute
)


class ProductAttributeInline(admin.TabularInline):
    model = ProductAttribute
    extra = 0


class ProductIngredientAdminInline(admin.TabularInline):
    model = ProductIngredient
    extra = 0


class ProductTagAdminInline(admin.TabularInline):
    model = ProductTag
    extra = 0


@admin.register(Category)
class CategoryAdmin(ModelAdmin):
    list_display = ['id', 'name', 'icon_tag']
    list_display_links = ['id', 'name']
    search_fields = ['id', 'name']


@admin.register(Ingredient)
class IngredientAdmin(ModelAdmin):
    list_display = ['id', 'name', 'icon_tag']
    list_display_links = ['id', 'name']
    search_fields = ['id', 'name']


@admin.register(Tag)
class TagAdmin(ModelAdmin):
    list_display = ['id', 'name', 'icon_tag']
    list_display_links = ['id', 'name']
    search_fields = ['id', 'name']


@admin.register(Attribute)
class AttributeAdmin(ModelAdmin):
    list_display = ['id', 'name']
    list_display_links = ['id', 'name']
    search_fields = ['id', 'name']


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'category', 'new_product', 'in_stock', 'photo_tag']
    list_display_links = ['id', 'name']
    search_fields = ['id', 'name', 'category']
    list_filter = ['category',]
    list_editable = ['new_product', 'in_stock']
    inlines = [
        ProductAttributeInline,
        ProductIngredientAdminInline,
        ProductTagAdminInline
    ]
