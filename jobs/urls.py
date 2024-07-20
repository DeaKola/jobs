from django.urls import path
from . import views
urlpatterns=[
    path('',views.job_list,name="job_list"),
    path('<int:job_id>/',views.job_details,name='job_details'),
    path('<int:job_id>/apply/',views.apply,name='apply'),
]