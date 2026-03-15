from django.db import models
from modular_entity_mapping_system.base_model import TimeStampsModel
from vendor.models import Vendor
from product.models import Product

# Create your models here.
class VendorProductMapping(TimeStampsModel):
    vendor = models.ForeignKey(Vendor,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    primary_mapping = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    
    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['vendor','product'],
                name='unique_vendor_product'
            )
        ]
        
    def __str__(self):
        return f"{self.vendor.name}-{self.product.name}"