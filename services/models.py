from django.db import models
from vendors.models import VendorProfile

class Service(models.Model):
    vendor = models.ForeignKey(
        VendorProfile,
        on_delete=models.CASCADE,
        related_name='services'
    )
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)

    def __str__(self):
        return f"{self.name} ({self.vendor.business_name})"


class ServiceVariant(models.Model):
    service = models.ForeignKey(
        Service,
        related_name='variants',
        on_delete=models.CASCADE
    )
    name = models.CharField(max_length=100)  # Basic, Premium, Express
    price = models.DecimalField(max_digits=10, decimal_places=2)
    estimated_minutes = models.PositiveIntegerField()
    stock = models.PositiveIntegerField(help_text="Number of simultaneous bookings allowed")

    def __str__(self):
        return f"{self.service.name} - {self.name}"
