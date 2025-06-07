from rest_framework import generics
from .models import UserProfile, Plan, Recharge, Usage
from .serializers import UserProfileSerializer, PlanSerializer, RechargeSerializer, UsageSerializer

class UserProfileList(generics.ListAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer

class PlanList(generics.ListCreateAPIView):
    queryset = Plan.objects.all()
    serializer_class = PlanSerializer

class RechargeList(generics.ListCreateAPIView):
    queryset = Recharge.objects.all()
    serializer_class = RechargeSerializer

class UsageList(generics.ListCreateAPIView):
    queryset = Usage.objects.all()
    serializer_class = UsageSerializer
