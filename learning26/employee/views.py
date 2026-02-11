from django.shortcuts import render
from .models import Employee

def employeelist(request):
    # employees = Employee.objects.all() #select * from employee
    employees = Employee.objects.all().values()
    # employees = Employee.objects.all().values_list()
    print(employees)
    return render(request, 'employee/employeelist.html',{"employees":employees})    