from django.contrib import admin
from django.utils.html import format_html
from .models import Product

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('admin_image', 'name', 'category', 'price', 'stock', 'available', 'rating', 'released_on')
    list_editable = ('price', 'stock', 'available', 'rating')
    list_filter = ('category', 'available', 'rating')
    search_fields = ('name',)

    def admin_image(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" style="width:60px;height:60px;object-fit:cover;border-radius:4px;" />',
                obj.image.url
            )
        return '-'
    admin_image.short_description = 'Image'