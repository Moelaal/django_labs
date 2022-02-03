from django.contrib import admin
from itistudent.models import Intake,users,students

# Register your models here.

admin.site.register(users)
admin.site.register(students)
admin.site.register(Intake)
