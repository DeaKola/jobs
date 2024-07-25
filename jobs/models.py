from django.contrib.auth.hashers import make_password
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Company(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(max_length=1000)
    website = models.URLField()

    def __str__(self):
        return self.name

class Jobs(models.Model):
    job_title = models.CharField(max_length=200)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    location = models.CharField(max_length=200)
    description = models.TextField(max_length=1000)
    requirements = models.TextField(max_length=1000,default=" ")
    pub_date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='jobs/images/', null=True, blank=True)
    category = models.CharField(max_length=200,default='')

def __str__(self):
        return self.job_title

class Application(models.Model):
    job = models.ForeignKey(Jobs,on_delete=models.CASCADE)
    applicant = models.ForeignKey(User,on_delete=models.CASCADE)
    first_name = models.CharField(max_length=200,default=" ")
    last_name = models.CharField(max_length=200,default=" ")
    cover_letter = models.TextField(max_length=200)
    email = models.EmailField(max_length=200,default=' ')
    applied_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.applicant.username} applied for {self.job.job_title} job'

class SignIn(models.Model):
    first_name = models.CharField(max_length=200, default=" ")
    last_name = models.CharField(max_length=200, default=" ")
    username = models.CharField(max_length=200,default=" ")
    email = models.EmailField(max_length=200, default=' ')
    password =  models.CharField(max_length=200,default=' ')


    def __str__(self):
        return self.username
class LogIn(models.Model):
    username = models.CharField(max_length=200,default=" ")
    password =  models.CharField(max_length=200,default=' ')

    def __str__(self):
        return self.username


