from django.contrib import admin
from .models import UserProfile, Category,Budgeting,Status,IncomeTracking,ExpenseTracking,Billing

# Register your models here.
admin.site.register(UserProfile)
admin.site.register(Category)
admin.site.register(Budgeting)
admin.site.register(Billing)
admin.site.register(Status)
admin.site.register(IncomeTracking)
admin.site.register(ExpenseTracking)

