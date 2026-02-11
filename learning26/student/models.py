from django.db import models

# Create your models here.
class student(models.Model):
    studentname = models.CharField(max_length=110)
    studentage = models.IntegerField()
    studentcity = models.CharField(max_length=50)
    studentemail = models.EmailField()

    class Meta:
        db_table = "student"

    def __str__(self):
        return self.studentname    

class product(models.Model):
    productname = models.CharField(max_length=100)
    productprice = models.IntegerField()
    productdescription = models.CharField(max_length=50)
    productstock = models.PositiveIntegerField()
    productcolor = models.CharField(max_length= 50 ,null = True)


    class Meta:
        db_table = "product"

    def __str__(self):
        return self.productname    


class employee(models.Model):
    employee_name = models.CharField(max_length=50)
    employee_age = models.IntegerField()
    employee_role = models.CharField(max_length = 50)
    employee_salary = models.IntegerField()
    employee_exp = models.IntegerField()
    employee_gender = models.CharField(null = True)
    
    class Meta:
        db_table = "employee"

    
    def __str__(self):
        return self.employee_name


class studentprofile(models.Model):
    hobbies = (("reading","reading"),
               ("travel","travel"),
               ("music","music"))
    studentid = models.OneToOneField(student,on_delete = models.CASCADE)
    studenthobbies = models.CharField(max_length = 50,choices=hobbies)
    studentaddress = models.CharField(max_length=100)
    studentphone = models.IntegerField()
    studentgender = models.CharField(max_length=30)
    studentDOB = models.DateField()

    class Meta:
        db_table = "studentprofile"

    
    def __str__(self):
        return self.studentid.studentname


class category(models.Model):
    categoryname = models.CharField(max_length=50)
    categorydescription = models.TextField()
    categorystatus = models.BooleanField(default=True)

    class Meta:
        db_table = "category"

    
    def __str__(self):
        return self.categoryname


class service(models.Model):
    servicename = models.CharField(max_length = 40)
    servicedescription = models.CharField(max_length= 100)
    serviceprice = models.IntegerField()
    servicestatus = models.BooleanField(default=True)
    categoryid = models.ForeignKey(category,on_delete = models.CASCADE)

    class Meta:
        db_table = "service"
    
    
    def __str__(self):
        return self.servicename


