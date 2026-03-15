from django.db import models
from modular_entity_mapping_system.base_model import TimeStampsModel

# Create your models here.
class Course(TimeStampsModel):
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=50,unique=True)
    description = models.TextField(blank=True,null=True)
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.name
