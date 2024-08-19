from django.contrib import admin

from .models import Review, ReviewsMedia


class ReviewsMediaInline(admin.TabularInline):
    model = ReviewsMedia
    extra = 0


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['id', 'product', 'user', 'rate', 'create_date']
    list_display_links = ['id', 'product', 'user']
    list_filter = ['rate',]
    inlines = [ReviewsMediaInline]
