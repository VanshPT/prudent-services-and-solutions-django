# pssapp/serializers.py

from django.contrib.auth.models import User, Group
from rest_framework import serializers
from rest_framework import serializers
from .models import Contacts, JobEntry, JobDetail, JobApplications

class ContactsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contacts
        fields = '__all__'

class JobEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = JobEntry
        fields = '__all__'

class JobDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobDetail
        fields = '__all__'

class JobApplicationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobApplications
        fields = '__all__'
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'groups']

class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ['id', 'name']