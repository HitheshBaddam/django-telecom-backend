from django.contrib import admin
from .models import UserProfile
from .models import Plan
from .models import Recharge
from .models import Usage

admin.site.register(UserProfile)
admin.site.register(Plan)
admin.site.register(Recharge)
admin.site.register(Usage)
