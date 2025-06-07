from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15, unique=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.phone_number}"

class Plan(models.Model):
    name = models.CharField(max_length=100)
    data_limit_gb = models.DecimalField(max_digits=5, decimal_places=2)  # Example: 10.00 GB
    validity_days = models.IntegerField()  # Example: 28, 30
    price = models.DecimalField(max_digits=6, decimal_places=2)  # Example: 199.99

    def __str__(self):
        return f"{self.name} - {self.data_limit_gb}GB - £{self.price} for {self.validity_days} days"
    
class Recharge(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    plan = models.ForeignKey(Plan, on_delete=models.CASCADE)
    recharge_date = models.DateTimeField(auto_now_add=True)
    expiry_date = models.DateTimeField()

    def __str__(self):
        return f"{self.user.username} - {self.plan.name} ({self.recharge_date.date()})"

class Usage(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    data_used_gb = models.DecimalField(max_digits=5, decimal_places=2, default=0.0)
    call_minutes = models.IntegerField(default=0)
    sms_count = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.user.username} usage on {self.date}"
