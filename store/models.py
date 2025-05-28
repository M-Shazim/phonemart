from django.db import models

class Product(models.Model):
    CATEGORY_CHOICES = [
        ('phone', 'Phone'),
        ('case', 'Case'),
        ('accessory', 'Accessory'),
    ]

    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='products/')
    stock = models.PositiveIntegerField()
    tags = models.CharField(max_length=255, blank=True)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    is_special = models.BooleanField(default=False)

    def __str__(self):
        return self.title

class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

class Cart(models.Model):
    items = models.ManyToManyField(CartItem)
    created_at = models.DateTimeField(auto_now_add=True)

class Order(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    address = models.TextField()
    ordered_at = models.DateTimeField(auto_now_add=True)
