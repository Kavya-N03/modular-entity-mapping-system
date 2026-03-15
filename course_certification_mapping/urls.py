from django.urls import path
from .views import CourseCertificationMappingView,CourseCertificationMappingDetailView

urlpatterns=[
    path('course-certification-mappings/',CourseCertificationMappingView.as_view(),name="course-certification-mapping"),
    path('course-certification-mappings/<int:pk>/',CourseCertificationMappingDetailView.as_view(),name="course-certification-mapping-detail"),
]