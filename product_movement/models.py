from django.db import models

from location.models import Location
from product.models import Product


class ProductMovement(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    qty = models.IntegerField()

    from_location = models.ForeignKey(
        Location,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='moved_from'
    )
    to_location = models.ForeignKey(
        Location,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='moved_to'
    )

    def __str__(self):
        return f"{self.product.name} - {self.timestamp}"

    class Meta:
        ordering = ['timestamp']
