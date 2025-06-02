from django.db import models


class Location(models.Model):
    name = models.CharField(max_length=255)
    pin_code = models.IntegerField(unique=True, default=000000)
    address = models.TextField(blank=True, null=True)
    capacity = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
