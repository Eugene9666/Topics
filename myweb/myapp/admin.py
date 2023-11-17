from django.contrib import admin
from .models import Goods,DailyInOut,Transfer,Client,Login
from django.contrib import admin
from .models import Goods

@admin.register(Goods)
class GoodsAdmin(admin.ModelAdmin):
    list_display = ('productId', 'productName', 'series', 'quantity', 'dailystatus', 'created_at', 'modified_at', 'created_by', 'modified_by')
# Register your models here.

@admin.register(DailyInOut)
class DailyinOutAdmin(admin.ModelAdmin):
    list_display = ('Date','goodsInOut','productId','productName','countQuantity','purchaseQuantity','exportQuantity','status', 'created_at', 'modified_at', 'created_by', 'modified_by')

@admin.register(Transfer)
class TransferAdmin(admin.ModelAdmin):
    list_display = ('productId', 'productName', 'position1', 'position2', 'position3', 'quantity', 'reason', 'created_at', 'modified_at', 'created_by', 'modified_by')

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('client', 'exportDate', 'nonShipment', 'productId', 'productName', 'clientRequirement', 'unit', 'created_at', 'modified_at', 'created_by', 'modified_by')




