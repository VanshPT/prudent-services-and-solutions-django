from django.db import models

# Create your models here.
class Contacts(models.Model):
    contact_id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=70,default="")
    phone=models.CharField(max_length=30,default="")
    desc=models.CharField(max_length=10000,default="")

    def __str__(self):
        return self.name
class JobEntry(models.Model):
    sr_no=models.AutoField(primary_key=True)
    job_name=models.CharField(max_length=100)
    job_code=models.CharField(max_length=50)

    def __str__(self):
        return self.job_name
    
class JobDetail(models.Model):
    job = models.ForeignKey(JobEntry, on_delete=models.CASCADE)
    place=models.CharField(max_length=30)

    def __str__(self):
        return self.job.job_name
    
class JobApplications(models.Model):
    application_id=models.AutoField(primary_key=True)
    Name=models.CharField(max_length= 100,default="")
    Applied_For=models.CharField(max_length=300, default="")
    Email=models.EmailField(max_length=254,default="")
    PhoneNo=models.CharField(max_length=20,default="")
    Resume=models.FileField(upload_to='uploads/')

    def __str__(self):
        return self.Name