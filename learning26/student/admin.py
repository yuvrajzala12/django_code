from django.contrib import admin
from .models import student,product,employee,studentprofile,category,service
# Register your models here.
admin.site.register(student)
admin.site.register(product)
admin.site.register(employee)
admin.site.register(studentprofile)
admin.site.register(category)
admin.site.register(service)