from rest_framework import serializers
from .models import Category,IncomeTracking, UserProfile, ExpenseTracking,FinancialGoal, Budgeting, Status, Billing

class UserProfileSerializer(serializers.ModelSerializer):
 class Meta:
  queryset = UserProfile
  fiedls = '__all__'

class CategorySerializer(serializers.ModelSerializer):
 class Meta:
  model = Category
  fields = '__all__'

class StatusSerializer(serializers.ModelSerializer):
 class Meta:
  model = Status
  fields = '__all__'
  
class IncomeTrackingSerializer(serializers.ModelSerializer):
 # user = serializers.StringRelatedField(read_only=False)
 class Meta:
  model = IncomeTracking
  fields = ['id','income_amount', 'income_source', 'date', 'description', 'user_profile']
  
class ExpenseTrackingSerializer(serializers.ModelSerializer):
 class Meta:
  model = ExpenseTracking
  fields = '__all__'
  
class BudgetingSerializer(serializers.ModelSerializer):
 class Meta:
  model = Budgeting
  fields = '__all__'
  
  
class BillingSerializer(serializers.ModelSerializer):
 class Meta:
  model = Billing
  fields = '__all__'
  
class FinancialGoalSerializer(serializers.ModelSerializer):
 class Meta:
  model = FinancialGoal
  fields = '__all__'
  