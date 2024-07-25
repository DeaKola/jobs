from django.urls import path
from . import views

urlpatterns = [
    path('', views.job_list, name="job_list"),
    path('<int:job_id>/', views.job_details, name='job_details'),
    path('<int:job_id>/apply/', views.apply, name='apply'),
    path('home/', views.home, name='home'),
    path('sign_in/', views.sign_in, name='sign_in'),
    path('log_in/', views.log_in, name='log_in'),
    path('category/<str:category>/', views.job_list, name='job_list_by_category'),
]
