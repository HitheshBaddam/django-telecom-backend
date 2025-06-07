from django.urls import path
from . import api_views

urlpatterns = [
    path('users/', api_views.UserProfileList.as_view(), name='user-list'),
    path('plans/', api_views.PlanList.as_view(), name='plan-list'),
    path('recharges/', api_views.RechargeList.as_view(), name='recharge-list'),
    path('usage/', api_views.UsageList.as_view(), name='usage-list'),
]
