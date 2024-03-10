from django.db import models
from django.contrib.auth.models import AbstractUser



class User(AbstractUser):
    wallet = models.DecimalField(
        decimal_places=2, max_digits=12, default=10000)


class Product(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(null=True, blank=True)
    price = models.DecimalField(decimal_places=2, max_digits=12)
    stock_amount = models.IntegerField(default=0)

    def __str__(self) -> str:
        return f'{str(self.pk)}_{self.name}'


class Purchase(models.Model):
    client = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='purchase')
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name='purchase')
    product_amount = models.PositiveIntegerField()
    purchasing_time = models.DateField(auto_now_add=True)

    def __str__(self) -> str:
        return f'{str(self.pk)}_{self.product.name}'
