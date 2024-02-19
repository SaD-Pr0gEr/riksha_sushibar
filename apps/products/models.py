from django.conf import settings
from django.db import models
from django.templatetags.static import static
from django.utils.functional import cached_property
from django.utils.html import format_html
from django.utils.translation import gettext_lazy as _

from apps.products.validators import validate_icon


class AbstractAttribute(models.Model):
    name = models.CharField(_('name'), max_length=128)
    slug = models.SlugField(_('URL'), max_length=128)
    icon = models.FileField(
        _('icon'),
        validators=[validate_icon],
        null=True,
        blank=True
    )

    @cached_property
    def icon_tag(self):
        if self.icon:
            return format_html(
                f'<img src="{self.icon.url}" height="40" width="40" />'
            )
        admin_no_svg = static('admin/img/icon-no.svg')
        return format_html(f'<img src="{admin_no_svg}">')

    icon_tag.short_description = 'Icon'

    class Meta:
        abstract = True


class Category(AbstractAttribute):
    icon = models.FileField(
        _('icon'),
        validators=[validate_icon],
        null=True,
        blank=True,
        upload_to=settings.PRODUCT_CATEGORY_PHOTO_DIR
    )

    def __str__(self):
        return self.name

    def __repr__(self):
        return f'Category: {self.slug}'

    class Meta:
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')


class Ingredient(AbstractAttribute):
    icon = models.FileField(
        _('icon'),
        validators=[validate_icon],
        null=True,
        blank=True,
        upload_to=settings.PRODUCT_INGREDIENT_PHOTO_DIR
    )

    def __str__(self):
        return self.name

    def __repr__(self):
        return f'Ingredient: {self.slug}'

    class Meta:
        verbose_name = _('Ingredient')
        verbose_name_plural = _('Ingredients')


class Tag(AbstractAttribute):
    icon = models.FileField(
        _('icon'),
        validators=[validate_icon],
        null=True,
        blank=True,
        upload_to=settings.PRODUCT_TAG_PHOTO_DIR
    )

    def __str__(self):
        return self.name

    def __repr__(self):
        return f'Tag: {self.slug}'

    class Meta:
        verbose_name = _('Tag')
        verbose_name_plural = _('Tags')


class Attribute(models.Model):
    name = models.CharField(_('name'), max_length=128)

    def __str__(self):
        return self.name

    def __repr__(self):
        return f'Attribute: {self.name}'

    class Meta:
        verbose_name = _('Attribute')
        verbose_name_plural = _('Attributes')


class Product(models.Model):
    name = models.CharField(_('Product name'), max_length=128)
    category = models.ForeignKey(
        Category,
        verbose_name=_('Product category'),
        on_delete=models.CASCADE,
        related_name='category_products'
    )
    slug = models.SlugField(_('URL'), max_length=128)
    photo = models.ImageField(_('Photo'), upload_to=settings.PRODUCT_PHOTO_DIR)
    price = models.IntegerField(_('Price'))
    in_stock = models.BooleanField(_('Stock status'), default=True)
    new_product = models.BooleanField(_('New product'), default=True)

    @cached_property
    def photo_tag(self):
        return format_html(
            f'<img src="{self.photo.url}" height="50" width="75" />'
        )

    def __str__(self):
        return self.name

    def __repr__(self):
        return f'Product: {self.name}'

    class Meta:
        verbose_name = _('Product')
        verbose_name_plural = _('Products')


class ProductIngredient(models.Model):
    product = models.ForeignKey(
        Product,
        verbose_name=_('Product'),
        on_delete=models.CASCADE,
        related_name='product_ingredients'
    )
    ingredient = models.ForeignKey(
        Ingredient,
        verbose_name=_('Ingredient'),
        on_delete=models.CASCADE,
        related_name='ingredient_products'
    )

    def __str__(self):
        return f'{self.product_id}'

    def __repr__(self):
        return f'Product_ingr.: {self.product_id}-{self.ingredient_id}'

    class Meta:
        verbose_name = _('Product Ingredient')
        verbose_name_plural = _('Product Ingredients')


class ProductTag(models.Model):
    product = models.ForeignKey(
        Product,
        verbose_name=_('Product'),
        on_delete=models.CASCADE,
        related_name='product_tags'
    )
    tag = models.ForeignKey(
        Tag,
        verbose_name=_('Tag'),
        on_delete=models.CASCADE,
        related_name='tag_products'
    )

    def __str__(self):
        return f'{self.product_id}'

    def __repr__(self):
        return f'Product tag: {self.product_id}-{self.tag_id}'

    class Meta:
        verbose_name = _('Product tag')
        verbose_name_plural = _('Product tags')


class ProductAttribute(models.Model):
    product = models.ForeignKey(
        Product,
        verbose_name=_('Product'),
        on_delete=models.CASCADE,
        related_name='product_attributes'
    )
    attribute = models.ForeignKey(
        Attribute,
        verbose_name=_('Attribute'),
        on_delete=models.CASCADE,
        related_name='attribute_products'
    )
    value = models.CharField(_('Value'), max_length=64)

    def __str__(self):
        return f'{self.product_id}'

    def __repr__(self):
        return f'Product_attr: {self.product_id}-{self.attribute_id}'

    class Meta:
        verbose_name = _('Product attribute')
        verbose_name_plural = _('Product attributes')
