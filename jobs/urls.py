from django.urls import path
from .views import apply_job, job_detail, job_list

urlpatterns = [
    path('', job_list, name='job_list'),
    path('job/<int:pk>/', job_detail, name='job_detail'),
    path('job/<int:pk>/apply/', apply_job, name='apply_job'),
]