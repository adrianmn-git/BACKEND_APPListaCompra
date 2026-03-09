from django.db import models
from django.utils import timezone

class Product(models.Model):
    CATEGORY_CHOICES = [
        ("fruit", "Fruta"),
        ("vegetables", "Verduras"),
        ("meat", "Carne"),
        ("fish", "Pescado y marisco"),
        ("dairy", "Lácteos"),
        ("eggs", "Huevos"),
        ("bread", "Panadería"),
        ("cereals", "Cereales y desayuno"),
        ("pasta_rice", "Pasta y arroz"),
        ("legumes", "Legumbres"),
        ("frozen", "Congelados"),
        ("canned", "Conservas"),
        ("snacks", "Snacks y aperitivos"),
        ("sweets", "Dulces y repostería"),
        ("sauces", "Salsas y condimentos"),
        ("spices", "Especias"),
        ("oil_vinegar", "Aceite y vinagre"),
        ("drinks", "Bebidas"),
        ("alcohol", "Alcohol"),
        ("cleaning", "Limpieza del hogar"),
        ("hygiene", "Higiene personal"),
        ("baby", "Bebé"),
        ("pets", "Mascotas"),
        ("other", "Otros"),
    ]

    name = models.CharField(max_length=150, unique=True)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        self.name = self.name.lower().strip()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class ShoppingList(models.Model):
    SHOPPING_CHOICES = [
        ("mercadona", "Mercadona"),
        ("alcampo", "Alcampo"),
        ("sorli", "Sorli"),
        ("esclat", "Esclat"),
        ("bonpreusa", "Bonpreu"),
        ("caprabo", "Caprabo"),
        ("carrefour", "Carrefour"),
    ]

    name = models.CharField(max_length=150)
    shop = models.CharField(max_length=10, choices=SHOPPING_CHOICES, default="mercadona")
    created_at = models.DateTimeField(auto_now_add=True)
    closed_at = models.DateTimeField(null=True, blank=True)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if self.completed and self.closed_at is None:
            self.closed_at = timezone.now()
        super().save(*args, **kwargs)

class ShoppingListItem(models.Model):
    UNIT_CHOICES = [
        ("unit", "Unidades"),
        ("kg", "Kilogramos"),
        ("g", "Gramos"),
        ("l", "Litros"),
        ("ml", "Mililitros"),
    ]

    shopping_list = models.ForeignKey(ShoppingList, on_delete=models.CASCADE, related_name="items")
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)
    unit = models.CharField(max_length=10, choices=UNIT_CHOICES, default="unit")
    picked_up = models.BooleanField(default=False)
    added_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.product.name} ({self.quantity})"

    class Meta:
        unique_together = ["shopping_list", "product"]