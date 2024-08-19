import os

from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.products.models import Product


class RateChoices(models.IntegerChoices):
    VERY_BAD = (1, _('Очень плохо'))
    BAD = (2, _('Плохо'))
    MID_BAD = (3, _('Удовлетворительно'))
    GOOD = (4, _('Хорошо'))
    EXCELLENT = (5, _('Отлично'))


class Review(models.Model):
    product = models.ForeignKey(
        Product,
        verbose_name=_('Product'),
        related_name='product_reviews',
        on_delete=models.CASCADE
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name=_('User'),
        related_name='user_reviews',
        on_delete=models.SET_NULL,
        null=True,
    )
    review = models.TextField(_('Review'))
    rate = models.IntegerField(
        _('Rate'),
        choices=RateChoices.choices
    )
    create_date = models.DateTimeField(
        _('Created date'),
        auto_now_add=True
    )

    def __str__(self):
        return f'{self.id}'

    def __repr__(self):
        return f'Review: {self.id}-{self.user_id}'

    class Meta:
        verbose_name = _('Review')
        verbose_name_plural = _('Product Reviews')


class ReviewsMedia(models.Model):
    review = models.ForeignKey(
        Review,
        verbose_name='Review',
        related_name='review_files',
        on_delete=models.CASCADE
    )
    file = models.FileField(
        _('File'),
        upload_to=settings.PRODUCT_REVIEWS_DIR
    )

    def delete(self, using=None, keep_parents=False):
        os.remove(self.file.path)
        return super().delete(using, keep_parents)

    def __str__(self):
        return f'{self.review_id}'

    def __repr__(self):
        return f'Review photo: {self.id}-{self.review_id}'

    class Meta:
        verbose_name = _('File')
        verbose_name_plural = _('Product Review files')
