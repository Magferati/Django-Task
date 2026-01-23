from django.db import transaction
from services.models import ServiceVariant

def reserve_stock(variant_id):
    with transaction.atomic():
        variant = ServiceVariant.objects.select_for_update().get(id=variant_id)
        if variant.stock <= 0:
            raise Exception("Out of stock")
        variant.stock -= 1
        variant.save()
