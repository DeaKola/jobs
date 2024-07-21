from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from .forms import ApplicationForm
from django.contrib.auth.decorators import login_required


from .models import Jobs,Application


# Create your views here.
def job_list(request):
  jobs= Jobs.objects.all()
  return render(request,'jobs/job_list.html',{'jobs':jobs})

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
         return redirect('job_list')
   else:
      form = ApplicationForm()
   return render(request,'jobs/apply.html',{'form':form,'job':job})