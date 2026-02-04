from django.db import models

# Create your models here.
class student(models.Model):
    studentname = models.CharField(max_length=110)
    studentage = models.IntegerField()
    studentcity = models.CharField(max_length=50)
    studentemail = models.EmailField()

    class meta:
        db_table = "student"

class product(models.Model):
    productname = models.CharField(max_length=100)
    productprice = models.IntegerField()
    productdescription = models.CharField(max_length=50)
    productstock = models.PositiveIntegerField()
    productcolor = models.CharField(max_length= 50 ,null = True)

    class meta:
        db_table = "product"
class employee(models.Model):
    employee_name = models.CharField(max_length=50)
    employee_age = models.IntegerField()
    employee_role = models.CharField(max_length = 50)
    employee_salary = models.IntegerField()
    employee_exp = models.IntegerField()
    employee_gender = models.CharField(null = True)
    
    class meta:
        db_table = "employee"
