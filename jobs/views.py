import django.contrib.messages
from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from .forms import ApplicationForm, SignInForm, LogInForm
from django.contrib.auth.decorators import login_required


from .models import Jobs,Application


# Create your views here.
def job_list(request,category=None):
    if category:
        jobs = Jobs.objects.filter(category__iexact=category)
    else:
        jobs = Jobs.objects.all()
    return render(request, 'jobs/job_list.html', {'jobs': jobs, 'selected_category': category})
def home(request):
   return render(request,'jobs/home.html')

def job_details(request,job_id):
   job = get_object_or_404(Jobs,id=job_id)
   return render(request,'jobs/job_details.html',{'job':job})

def apply(request,job_id):
   job = get_object_or_404(Jobs,id=job_id)
   if request.method == 'POST':
      form=ApplicationForm(request.POST)
      if form.is_valid():
         application = form.save(commit=False)
         application.job = job
         application.applicant = request.user
         application.save()
         messages.success(request, 'Your application was submitted successfully!')
         return redirect('job_list')
   else:
      form = ApplicationForm()
   return render(request,'jobs/apply.html',{'form':form,'job':job})


def sign_in(request):
  if request.method == 'POST':
      form = SignInForm(request.POST)
      if form.is_valid():
         form.save()
         messages.success(request, 'Your account was created successfully!')
         return redirect('sign_in')
  else:
      form = SignInForm()
  return render(request, 'jobs/sign_in.html', {'form': form})

def log_in(request):
    if request.method=='POST':
        form = LogInForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'You have been logged in successfully!')
            return redirect('log_in')
    else:
         form = LogInForm()
    return render(request, 'jobs/log_in.html', {'form': form})