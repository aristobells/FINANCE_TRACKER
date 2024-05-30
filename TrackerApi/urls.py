from django.urls import path
from . import views

urlpatterns =[
   path('', views.FinancialGoalView.as_view()),
   path('category', views.CategoryView.as_view()),
   path('category/<int:pk>', views.SingleCategoryView.as_view()),
   path('status', views.StatusView.as_view()),
   path('status/<int:pk>', views.SingleStatusView.as_view()),
   path('income', views.IncomeTrackingView.as_view()),
   path('income/<int:pk>', views.SingleIncomeTracking.as_view()),
   path('expense', views.ExpenseTrackingView.as_view()),
   path('expense/<int:pk>', views.SingleExpenseTrackingView.as_view()),
   path('budget', views.BudgetingView.as_view()),
   path('budget/<int:pk>', views.SingleBudgetingView.as_view()),
   path('billing', views.BillingView.as_view()),
   path('billing/<int:pk>', views.SingleBillingView.as_view()),
   path('fin_goal', views.FinancialGoalView.as_view()),
   path('fin_goal/<int:pk>', views.SingleFinancialGoalView.as_view()),

]