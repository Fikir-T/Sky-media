from django.contrib import admin
from .models import orders, contact_us

# Register your models here.
admin.site.register(orders)
admin.site.register(contact_us)