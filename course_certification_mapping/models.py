from django.db import models
from modular_entity_mapping_system.base_model import TimeStampsModel
from course.models import Course
from certification.models import Certification

# Create your models here.
class CourseCertificationMapping(TimeStampsModel):
    course = models.ForeignKey(Course,on_delete=models.CASCADE)
    certification = models.ForeignKey(Certification,on_delete=models.CASCADE)
    primary_mapping = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    
    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['course','certification'],
                name="unique_course_certification"
            )
        ]
    
    def __str__(self):
        return f"{self.course.name}-{self.certification.name}"