from django.db import models

class students(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    track=models.CharField(max_length=20)

class Intake(models.Model):
    id =models.AutoField(primary_key=True)
    fullname =models.CharField(max_length=20)
    sdate =models.DateField()
    edate =models.DateField()


class Track(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=50)

class users(models.Model):
    username=models.CharField(max_length=30)
    password=models.CharField(max_length=20)