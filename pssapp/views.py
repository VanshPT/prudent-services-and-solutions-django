from django.shortcuts import render
from django.http import HttpResponse
from .models import Contacts,JobDetail,JobEntry,JobApplications
# Create your views here.
def index(request):
    return render(request,"pssapp/index.html")
def about(request):
    return render(request,"pssapp/about.html")
def ourprocesses(request):
    return render(request,"pssapp/ourprocesses.html")
def valuedpartners(request):
    return render(request,"pssapp/valuedpartners.html")
def contact(request):
    return render(request,"pssapp/contact.html")
def getback(request):
    if request.method=="POST":
        name=request.POST.get('Name','')
        email=request.POST.get('Email','')
        phone=request.POST.get('Phone','')
        message=request.POST.get('Message','')
        contacts=Contacts(name=name,email=email,phone=phone,desc=message)
        contacts.save()


        filler_name=request.POST.get('Name','')
        filler_jobname=request.POST.get('JobName','')
        filler_email=request.POST.get('Email','')
        filler_phone=request.POST.get('Phone','')
        filler_resume=request.FILES.get('Resume','')
        print(filler_resume)
        jobApplications=JobApplications(Name=filler_name,Applied_For=filler_jobname,Email=filler_email,PhoneNo=filler_phone,Resume=filler_resume)
        jobApplications.save()
    return render(request,"pssapp/getback.html")
def careers(request):
    jobsavail = JobDetail.objects.values("job", "place")
    jobname = JobEntry.objects.values("sr_no", "job_name")

    # Create a dictionary to map sr_no to job_name
    jobname_mapping = {job['sr_no']: job['job_name'] for job in jobname}

    # Iterate through jobsavail and add the 'job_name' key
    for job in jobsavail:
        job_id = job['job']
        if job_id in jobname_mapping:
            job['job_name'] = jobname_mapping[job_id]

    params = {'jobs': jobsavail}
    return render(request, "pssapp/careers.html", params)

def jobseeker(request):
    if request.method == 'POST':
        job=request.POST.get('jobname','')
        params={'job':job}
    return render(request,'pssapp/jobseekerform.html',params)

