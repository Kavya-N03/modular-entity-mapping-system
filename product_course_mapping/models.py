from django.db import models
from modular_entity_mapping_system.base_model import TimeStampsModel
from product.models import Product
from course.models import Course

# Create your models here.
class ProductCourseMapping(TimeStampsModel):
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    course = models.ForeignKey(Course,on_delete=models.CASCADE)
    primary_mapping = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    
    class Meta:
        constraints=[
            models.UniqueConstraint(
                fields=['product','course'],
                name = "unique_product_course"
            )
        ]
    
    def __str__(self):
        return f"{self.product.name}-{self.course.name}"