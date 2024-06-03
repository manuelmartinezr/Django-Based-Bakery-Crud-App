from django.contrib import admin
from .models import *

admin.site.register(Customer)
admin.site.register(DeliveryPerson)
admin.site.register(DeliverySchedules)
admin.site.register(DeliveryVehicle)
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Administrator)
# Register your models here.
