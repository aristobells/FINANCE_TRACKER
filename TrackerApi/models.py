from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserProfile(models.Model):
 user = models.OneToOneField(User,on_delete=models.CASCADE)
 mobile = models.CharField(max_length=20)
 address = models.CharField(max_length=200)

 def __str__(self):
  return self.user.username


class Category(models.Model):
 slug = models.SlugField()
 title =models.CharField(max_length=255)
 
 def __str__(self):
  return self.title
 
class IncomeTracking(models.Model):
 user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
 income_amount = models.DecimalField(max_digits=10, decimal_places=2)
 date = models.DateTimeField(auto_now_add=True)
 income_source = models.CharField(max_length=100)
 description = models.TextField(blank=True)
 
class ExpenseTracking(models.Model):
 amount = models.DecimalField(max_digits=20,decimal_places=2)
 category =models.ForeignKey(Category,on_delete=models.PROTECT)
 date = models.DateTimeField(auto_now_add=True)
 description = models.TextField(blank=True)
 user_profile = models.ForeignKey(UserProfile,on_delete=models.CASCADE) 
 income = models.ForeignKey(IncomeTracking,on_delete=models.CASCADE)
 
class Budgeting(models.Model):
 budgeted_amount = models.DecimalField(max_digits=20, decimal_places=2)
 start_date = models.DateTimeField()
 end_date = models.DateTimeField()
 category = models.ForeignKey(Category, on_delete=models.PROTECT)
 user_profile = models.ForeignKey(UserProfile,on_delete=models.CASCADE)
 
class Status(models.Model):
 slug = models.SlugField()
 title = models.CharField(max_length=100)
 
 def __str__(self):
  return self.title
 
class Billing(models.Model):
 bill_description = models.CharField(max_length=225, blank=True)
 bill_amount = models.DecimalField(max_digits=20,decimal_places=2)
 due_date = models.DateTimeField()
 status = models.ForeignKey(Status,on_delete=models.SET_NULL, null=True)
 user_profile = models.ForeignKey(UserProfile,on_delete=models.CASCADE)
 category = models.ForeignKey(Category,on_delete=models.CASCADE, default=1)
 
 
 
class FinancialGoal(models.Model):
 goal_amount = models.DecimalField(max_digits=20, decimal_places=2)
 target_date = models.DateTimeField()
 description = models.TextField(blank=True)
 user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
 
 
