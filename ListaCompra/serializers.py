from rest_framework import serializers
from .models import Product, ShoppingList, ShoppingListItem


class ProductSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(source="category.name", read_only=True)

    class Meta:
        model = Product
        fields = ["id", "name", "category", "created_at"]


class ShoppingListSerializer(serializers.ModelSerializer):
    items_count = serializers.SerializerMethodField()

    class Meta:
        model = ShoppingList
        fields = ["id", "name", "shop", "created_at", "completed", "items_count"]

    def get_items_count(self, obj):
        return obj.items.count()


class ShoppingListItemSerializer(serializers.ModelSerializer):
    product_name = serializers.CharField(source="product.name", read_only=True)

    class Meta:
        model = ShoppingListItem
        fields = ["id", "shopping_list", "product", "product_name", "quantity", "unit", "picked_up", "added_at"]