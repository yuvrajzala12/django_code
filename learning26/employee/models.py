from django.db import models

# Create your models here.
class Employee(models.Model):
    Employeename = models.CharField(max_length=50)
    Employeeid = models.IntegerField(null=True)
    Employee_salary = models.IntegerField(null=True)
    Employee_exp = models.IntegerField(null=True)

    class Meta:
        db_table = "Employee"

    def __str__(self):
        return self.Employeename