from django.contrib import admin
from .models import Goods,DailyInOut,Transfer,Client,Login
from django.contrib import admin
from .models import Goods

@admin.register(Goods)
class GoodsAdmin(admin.ModelAdmin):
    list_display = ('productId', 'productName', 'series', 'quantity', 'dailystatus', 'created_at', 'modified_at', 'created_by', 'modified_by')
    search_fields = ('productName','productId', 'series')  # 根據 'productName' 和 'series' 欄位搜尋

@admin.register(DailyInOut)
class DailyinOutAdmin(admin.ModelAdmin):
    list_display = ('Date','goodsInOut','productId','productName','countQuantity','purchaseQuantity','exportQuantity','status', 'created_at', 'modified_at', 'created_by', 'modified_by')
    search_fields = ('productName','productId', 'status')  # 根據 'productName' 和 'status' 欄位搜尋

@admin.register(Transfer)
class TransferAdmin(admin.ModelAdmin):
    list_display = ('productId', 'productName', 'position1', 'position2', 'position3', 'quantity', 'reason', 'created_at', 'modified_at', 'created_by', 'modified_by')
    search_fields = ('productName','productId', 'reason')  # 根據 'productName' 和 'reason' 欄位搜尋

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('client', 'exportDate', 'nonShipment', 'productId', 'productName', 'clientRequirement', 'unit', 'created_at', 'modified_at', 'created_by', 'modified_by')
    search_fields = ('client','productId', 'productName')  # 根據 'client' 和 'productName' 欄位搜尋

@admin.register(Login)
class LoginAdmin(admin.ModelAdmin):
    list_display = ('userName','password','level','Name')
    search_fields = ('userName', 'level')


