from django.contrib import admin
from .models import (
    Product,
    Category,
    Images,
    Cart,
    CartItem
)

class ImagesInline(admin.TabularInline):
    model = Images


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [
        ImagesInline
    ]

class CartItemInline(admin.TabularInline):
    model = CartItem

@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    inlines = [
        CartItemInline
    ]


admin.site.register(Category)
admin.site.register(Images)
admin.site.register(CartItem)