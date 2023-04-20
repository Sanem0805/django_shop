from django.contrib import admin
from .models import Order, OrderItem

class TabularOrderItem(admin.TabularInline):
    model = OrderItem
    extra = 1

@admin.register(Order)
class OrederAdmin(admin.ModelAdmin):
    inlines = [TabularOrderItem]
