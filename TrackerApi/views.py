from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.exceptions import PermissionDenied
from .models import Category, IncomeTracking, ExpenseTracking, Budgeting,Status,Billing, FinancialGoal, UserProfile
from .serializers import CategorySerializer,IncomeTrackingSerializer, ExpenseTrackingSerializer,BudgetingSerializer,BillingSerializer, StatusSerializer,FinancialGoalSerializer, UserProfileSerializer
from rest_framework.permissions import IsAuthenticated, BasePermission
from django.shortcuts import get_object_or_404
from rest_framework import filters
# Create your views here.

class CategoryView(generics.ListCreateAPIView):
 permission_classes =[IsAuthenticated]
 queryset = Category.objects.all()
 serializer_class = CategorySerializer
 
 def create(self, request, *args, **kwargs):
  if (self.request.user.groups.filter(name='Manager').exists() or self.request.user.is_superuser):
      serialized_item = CategorySerializer(data=self.request.data)
      serialized_item.is_valid(raise_exception=True)
      serialized_item.save()
      return Response(serialized_item.data, status=status.HTTP_201_CREATED)
  else:
      return Response(
          {"error": "Only Managers are allowed to create categories."},
          status=status.HTTP_403_FORBIDDEN
      )
      
# Customized permission class
class IsManagerOrSuperUser(BasePermission):
 def has_permission(self, request, view):
  return request.user.groups.filter(name ='Manager').exists() or request.user.is_superuser

class SingleCategoryView(generics.RetrieveUpdateDestroyAPIView):
 permission_classes =[IsAuthenticated, IsManagerOrSuperUser]
 queryset = Category.objects.all()
 serializer_class = CategorySerializer

# Status Views
class StatusView(generics.ListCreateAPIView):
 queryset = Status.objects.all()
 serializer_class = StatusSerializer
 
 def create(self, request, *args, **kwargs):
  if (self.request.user.groups.filter(name='Manager').exists() or self.request.user.is_superuser):
      serialized_item = StatusSerializer(data=self.request.data)
      serialized_item.is_valid(raise_exception=True)
      serialized_item.save()
      return Response(serialized_item.data, status=status.HTTP_201_CREATED)
  else:
      return Response(
          {"error": "Only Managers are allowed to create status."},
          status=status.HTTP_403_FORBIDDEN
      )
class SingleStatusView(generics.RetrieveUpdateDestroyAPIView):
 permission_classes =[IsAuthenticated, IsManagerOrSuperUser]
 queryset = Status.objects.all()
 serializer_class = StatusSerializer
 
# Income Tracking views 
class IncomeTrackingView(generics.ListCreateAPIView):
#  queryset = IncomeTracking.objects.select_related('user_profile').all()
 serializer_class = IncomeTrackingSerializer
 permission_classes = [IsAuthenticated]
 ordering_fields = ['income_amount','date']
 search_fields=['description']
 
 def get_queryset(self):
   if self.request.user.groups.filter(name='Manager').exists() or self.request.user.is_superuser:
       return IncomeTracking.objects.all()
   else: 
       return IncomeTracking.objects.all().filter(user_profile = self.request.user.userprofile)
 
class SingleIncomeTracking(generics.RetrieveUpdateDestroyAPIView):
 queryset= IncomeTracking.objects.all()
 permission_classes = [IsAuthenticated]
 serializer_class =IncomeTrackingSerializer
 
 def get_queryset(self):
   if self.request.user.groups.filter(name='Manager').exists():
       raise PermissionDenied(detail='Managers cannot edit, delete, or retrieve customer income.', code=status.HTTP_403_FORBIDDEN)
   elif self.request.user.is_superuser:
       return IncomeTracking.objects.all()
   else:
       return IncomeTracking.objects.all().filter(user_profile = self.request.user.userprofile)
       

# Expense Tracking views
class ExpenseTrackingView(generics.ListCreateAPIView):
 queryset = ExpenseTracking.objects.all()
 permission_classes = [IsAuthenticated]
 serializer_class = ExpenseTrackingSerializer
 ordering_fields = ['income_amount','category__title']
 search_fields=['description']
 
 def get_queryset(self):
   if self.request.user.groups.filter(name='Manager').exists() or self.request.user.is_superuser:
       return ExpenseTracking.objects.all()
   else: 
       return ExpenseTracking.objects.all().filter(user_profile = self.request.user.userprofile)
     
 
class SingleExpenseTrackingView(generics.RetrieveUpdateDestroyAPIView):
 queryset= ExpenseTracking.objects.all()
 permission_classes = [IsAuthenticated]
 serializer_class = ExpenseTrackingSerializer
 def get_queryset(self):
   if self.request.user.groups.filter(name='Manager').exists():
       raise PermissionDenied(detail='Managers cannot edit, delete, or retrieve customer income.', code=status.HTTP_403_FORBIDDEN)
   elif self.request.user.is_superuser:
       return ExpenseTracking.objects.all()
   else:
       return ExpenseTracking.objects.all().filter(user_profile = self.request.user.userprofile)
 
 
# Budgeting Views
class BudgetingView(generics.ListCreateAPIView):
 queryset =Budgeting.objects.all()
 permission_classes = [IsAuthenticated]
 serializer_class = BudgetingSerializer
 ordering_fields = ['income_amount','category__title']
 search_fields=['description']
 
 def get_queryset(self):
   if self.request.user.groups.filter(name='Manager').exists() or self.request.user.is_superuser:
       return Budgeting.objects.all()
   else: 
       return Budgeting.objects.all().filter(user_profile = self.request.user.userprofile)
 
class SingleBudgetingView(generics.RetrieveUpdateDestroyAPIView):
 queryset= Budgeting.objects.all()
 permission_classes = [IsAuthenticated]
 serializer_class = BudgetingSerializer
 
 def get_queryset(self):
   if self.request.user.groups.filter(name='Manager').exists():
       raise PermissionDenied(detail='Managers cannot edit, delete, or retrieve customer income.', code=status.HTTP_403_FORBIDDEN)
   elif self.request.user.is_superuser:
       return Budgeting.objects.all()
   else:
       return Budgeting.objects.all().filter(user_profile = self.request.user.userprofile)

# Billing Views
class BillingView(generics.ListCreateAPIView):
 queryset =Billing.objects.all() 
 permission_classes = [IsAuthenticated]
 serializer_class = BillingSerializer
 ordering_fields = ['status']
 search_fields=['status__title']
 
 def get_queryset(self):
   if self.request.user.groups.filter(name='Manager').exists() or self.request.user.is_superuser:
       return Billing.objects.all()
   else: 
       return Billing.objects.all().filter(user_profile = self.request.user.userprofile)

 def create(self, request, *args, **kwargs):
    if self.request.user.groups.filter(name = 'Manager').exists():
        return Response({'message': 'managers are not allowed to perform this operation'}, status.HTTP_401_UNAUTHORIZED)
    else:
        data = self.request.data
        serialized_item = BillingSerializer(data=data)
        serialized_item.is_valid(raise_exception=True)
        billing_instance = serialized_item.save()
        
        if billing_instance.status.title  == 'Paid':
            # Get the first associated IncomeTracking instance with the UserProfile for the current billing
            income_tracking_instance = billing_instance.user_profile.incometracking_set.first()
            if income_tracking_instance:
                expense_data = {
                    'amount' : billing_instance.bill_amount,
                    'category': billing_instance.category.id,
                    'description': billing_instance.bill_description,
                    'user_profile': billing_instance.user_profile.id,
                    'income': income_tracking_instance.id
                    
                }
                expense_serializer = ExpenseTrackingSerializer(data=expense_data)
                expense_serializer.is_valid(raise_exception=True)
                expense_serializer.save()
                return Response({'message': 'Billing and Expense Created successfully'}, status= status.HTTP_201_CREATED)
            else:
                return Response({'Error':'User must have an income'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'message': 'Billing created successfully'}, status=status.HTTP_201_CREATED)  
        
        
class SingleBillingView(generics.RetrieveUpdateDestroyAPIView):
 queryset= Billing.objects.all()
 permission_classes = [IsAuthenticated]
 serializer_class = BillingSerializer
 
 def get_queryset(self):
   if self.request.user.groups.filter(name='Manager').exists():
       raise PermissionDenied(detail='Managers cannot edit, delete, or retrieve customer income.', code=status.HTTP_403_FORBIDDEN)
   elif self.request.user.is_superuser:
       return Billing.objects.all()
   else:
       return Billing.objects.all().filter(user_profile = self.request.user.userprofile)
 def update(self, request, *args, **kwargs):
    if self.request.user.groups.filter(name='Manager').exists():
       raise PermissionDenied(detail='Managers cannot edit, delete, or retrieve customer income.', code=status.HTTP_403_FORBIDDEN)
   
    instance = self.get_object()
    serializer = BillingSerializer(instance, data=request.data, partial=True)
    serializer.is_valid(raise_exception=True)
    update_instance = serializer.save()
    if  update_instance.status.title == 'Paid':
        #  Retrieve associated ExpenseTracking instance based on billing details
        expense_instance = ExpenseTracking.objects.filter(
        amount=update_instance.bill_amount,
        category=update_instance.category,
        description=update_instance.bill_description,
        user_profile=update_instance.user_profile
).first()
        # if an expense_instance exist, update its data
        income_tracking_instance = update_instance.user_profile.incometracking_set.first()
        if expense_instance:
            expense_data ={
                'amount': update_instance.bill_amount,
                'category': update_instance.category.id,
                'description' : update_instance.bill_description,
                'user_profile': update_instance.user_profile.id,
                'income': income_tracking_instance.id
            }
            expense_serializer =ExpenseTrackingSerializer(instance=expense_instance,data=expense_data, partial=True)
            expense_serializer.is_valid(raise_exception=True)
            expense_serializer.save()
            return Response({'message': 'Expense and Billing Updated successfully'}, status.HTTP_201_CREATED)
    # Get the first associated IncomeTracking instance with the UserProfile for the current billing
        income_tracking_instance = update_instance.user_profile.incometracking_set.first()
        if income_tracking_instance:
            expense_data = {
                'amount' : update_instance.bill_amount,
                'category': update_instance.category.id,
                'description': update_instance.bill_description,
                'user_profile': update_instance.user_profile.id,
                'income': income_tracking_instance.id
                
            }
            expense_serializer = ExpenseTrackingSerializer(data=expense_data)
            expense_serializer.is_valid(raise_exception=True)
            expense_serializer.save()
            return Response({'message': 'Billing Updated and Expense Created successfully'}, status= status.HTTP_201_CREATED)
        else:
                return Response({'Error':'User must have an income'}, status=status.HTTP_400_BAD_REQUEST)
    else:
            return Response({'message': 'Billing Updated successfully'}, status=status.HTTP_201_CREATED)
            
        
 
# Financial Goal
class FinancialGoalView(generics.ListCreateAPIView):
 queryset =FinancialGoal.objects.all()
 serializer_class = FinancialGoalSerializer
 permission_classes =[IsAuthenticated]
 def get_queryset(self):
   if self.request.user.groups.filter(name='Manager').exists() or self.request.user.is_superuser:
       return FinancialGoal.objects.all()
   else: 
       return FinancialGoal.objects.all().filter(user_profile = self.request.user.userprofile)
 
class SingleFinancialGoalView(generics.RetrieveUpdateDestroyAPIView):
 queryset= FinancialGoal.objects.all()
 serializer_class = FinancialGoalSerializer
 permission_classes =[IsAuthenticated]
 
 def get_queryset(self):
   if self.request.user.groups.filter(name='Manager').exists():
       raise PermissionDenied(detail='Managers cannot edit, delete, or retrieve customer income.', code=status.HTTP_403_FORBIDDEN)
   elif self.request.user.is_superuser:
       return FinancialGoal.objects.all()
   else:
       return FinancialGoal.objects.all().filter(user_profile = self.request.user.userprofile)
   


