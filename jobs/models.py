from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Company(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(max_length=200)
    website = models.URLField()

    def __str__(self):
        return self.name

class Jobs(models.Model):
    job_title = models.CharField(max_length=200)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    location = models.CharField(max_length=200)
    description = models.TextField(max_length=200)
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.job_title

class Application(models.Model):
    job = models.ForeignKey(Jobs,on_delete=models.CASCADE)
    applicant = models.ForeignKey(User,on_delete=models.CASCADE)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    cover_letter = models.TextField(max_length=200)
    email = models.EmailField(max_length=200)
    applied_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.applicant.username} applied for {self.job.job_title} job'