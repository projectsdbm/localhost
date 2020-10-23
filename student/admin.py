from django.contrib import admin
from .models import DepartmentModel, StudentModel
# Register your models here.
admin.site.register(DepartmentModel)
admin.site.register(StudentModel)
