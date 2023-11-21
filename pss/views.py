from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets
from rest_framework import permissions
from pssapp.models import Contacts, JobDetail, JobEntry, JobApplications
from pssapp.serializers import ContactsSerializer, JobDetailSerializer, JobEntrySerializer, JobApplicationsSerializer, UserSerializer, GroupSerializer
from django.contrib.auth.models import User, Group


def index(request):
    return render(request,'index.html')
class ContactsViewSet(viewsets.ModelViewSet):
    queryset = Contacts.objects.all()
    serializer_class = ContactsSerializer

class JobEntryViewSet(viewsets.ModelViewSet):
    queryset = JobEntry.objects.all()
    serializer_class = JobEntrySerializer

class JobDetailViewSet(viewsets.ModelViewSet):
    queryset = JobDetail.objects.all()
    serializer_class = JobDetailSerializer

class JobApplicationsViewSet(viewsets.ModelViewSet):
    queryset = JobApplications.objects.all()
    serializer_class = JobApplicationsSerializer

# Default views for User and Group

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]