from itertools import product
from logging import NullHandler
from statistics import mode
from tkinter import CASCADE
from django.db import models
from django.db import models
from django.contrib.auth.models import User

class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='created_%(class)s_set')
    modified_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='modified_%(class)s_set')

    class Meta:
        abstract = True


# Create your models here.
class Goods (TimeStampedModel):
    productId = models.CharField('產品ID',max_length=100 , unique=True, primary_key=True)
    productName = models.CharField('產品名稱',max_length=100)
    series = models.CharField('系列',max_length=30)
    quantity = models.IntegerField('入數')
    dailystatus = models.CharField("庫存資訊&調貨狀況",max_length=500,default="",blank=True,null=True)

class DailyInOut (TimeStampedModel):
    Date = models.DateField("日期")
    goodsInOut = models.CharField("貨品進出狀況",max_length=500,null=True,blank=True)
    productId = models.CharField('產品ID',max_length=100)
    productName = models.CharField('產品名稱',max_length=100)
    countQuantity = models.FloatField("盤點數量(件)",null=True,blank=True,default=0)
    purchaseQuantity = models.FloatField("進貨數量(件)",null=True,blank=True,default=0)
    exportQuantity = models.FloatField("出貨數量(件)",null=True,blank=True,default=0)
    status = models.CharField("調貨狀況or進出貨資訊",max_length=500,null=True,blank=True)

class Transfer(TimeStampedModel):
    productId = models.CharField('產品ID',max_length=100 )
    productName = models.CharField('產品名稱',max_length=100)
    position1 = models.CharField("儲位1",max_length=10)
    position2 = models.CharField("儲位2",max_length=10, null=True,blank=True)
    position3 = models.CharField("儲位3",max_length=10, null=True,blank=True)
    quantity = models.FloatField("數量")
    reason = models.CharField("未調貨原因",max_length=500, null=True,blank=True)

class Client(TimeStampedModel):
    client = models.CharField("客戶",max_length=20)
    exportDate = models.DateField("出貨日期")
    nonShipment = models.CharField("未出貨原因",max_length=100,null=True)
    productId = models.CharField('產品ID',max_length=100)
    productName = models.CharField('產品名稱',max_length=100)
    clientRequirement = models.IntegerField("客戶需求數量")
    unit = models.CharField("單位",max_length=5)

USER_TYPE = (       
    ('admin','Admin'),
    ('user','User'),
    )

    

class Login(models.Model):
    userName = models.CharField("帳號",max_length=15)
    password = models.CharField("密碼",max_length=20)
    level = models.CharField("階級",max_length=10,choices=USER_TYPE, default="user")
    Name = models.CharField("用戶名稱",max_length=20)


