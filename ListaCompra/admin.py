from django.contrib import admin
from .models import Product, ShoppingList, ShoppingListItem


class ProductAdmin(admin.ModelAdmin):
    list_display = ["name", "category", "created_at"]
    search_fields = ["name"]
    list_filter = ["category"]


class ShoppingListItemInline(admin.TabularInline):
    model = ShoppingListItem
    extra = 1


class ShoppingListAdmin(admin.ModelAdmin):
    list_display = ["name", "created_at", "completed"]
    list_filter = ["completed"]
    inlines = [ShoppingListItemInline]


admin.site.register(Product, ProductAdmin)
admin.site.register(ShoppingList, ShoppingListAdmin)