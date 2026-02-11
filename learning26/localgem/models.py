from django.db import models

# Create your models here.
class user(models.Model):
    name = models.CharField(max_length=50)
    id = models.IntegerField()
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=50)
    role = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    # profile_pic = models.CharField(max_length=50)
    # acc_created_at = models.CharField(max_length=50)
    # acc_updated_at = models.CharField(max_length=50)

    class Meta:
        db_table = "user"
    
    def __str__(self):
        return self.name
    
class talent_profile(models.Model):
    t_id = models.IntegerField() 
    t_name = models.CharField(max_length=50) 
    t_skill = models.CharField(max_length=100) 
    t_exp = models.CharField(max_length=50) 
    t_available = models.CharField(max_length=50) 
    t_contact_info = models.CharField(max_length=50) 
    t_rating = models.CharField(max_length=50) 
    t_acc_created_at = models.CharField(max_length=50) 
    t_acc_updated_at = models.CharField(max_length=50) 

    class Meta:
        db_table = "talent_profile"

    def __str__(self):
        return self.t_name

class booking(models.Model):
    booking_id = models.IntegerField()
    id = models.CharField(max_length=50)        
    t_id = models.CharField(max_length=50)        
    event_date = models.DateField()      
    status = models.CharField(max_length=50)        
    acc_created_at = models.CharField(max_length=50) 

    class Meta:
        db_table = "booking"

    def __str__(self):
        return self.booking_id

class rating_review(models.Model):
    review_id = models.IntegerField()
    id = models.IntegerField()
    skill_needed = models.CharField(max_length=100)   
    event_date = models.DateField()   
    status = models.CharField(max_length=100)
    acc_created_at = models.CharField(max_length = 100)
    
    class Meta:
        db_table = "reting_review"

    def __str__(self):
        return self.review_id



class message(models.Model):
    message_id = models.IntegerField()                
    sender_id = models.IntegerField()                
    receiver_id = models.IntegerField()

    class Meta:
        db_table = "message"

    def __str__(self):
        return self.message_id                    




