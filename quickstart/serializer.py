
from django.contrib.auth import models
from django.contrib.auth.models import User
from itistudent.models import students,users
from rest_framework import serializers



class Userserializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = users
        fields = ['username']