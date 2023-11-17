# Generated by Django 4.2.7 on 2023-11-03 08:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Client",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("client", models.CharField(max_length=20, verbose_name="客戶")),
                ("exportDate", models.DateField(verbose_name="出貨日期")),
                (
                    "nonShipment",
                    models.CharField(max_length=100, null=True, verbose_name="未出貨原因"),
                ),
                ("productId", models.CharField(max_length=100, verbose_name="產品ID")),
                ("productName", models.CharField(max_length=100, verbose_name="產品名稱")),
                ("clientRequirement", models.IntegerField(verbose_name="客戶需求數量")),
                ("unit", models.CharField(max_length=5, verbose_name="單位")),
            ],
        ),
        migrations.CreateModel(
            name="DailyInOut",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("Date", models.DateField(verbose_name="日期")),
                ("goodsInOut", models.CharField(max_length=500, verbose_name="貨品進出狀況")),
                ("productId", models.CharField(max_length=100, verbose_name="產品ID")),
                ("productName", models.CharField(max_length=100, verbose_name="產品名稱")),
                ("countQuantity", models.FloatField(null=True, verbose_name="盤點數量(件)")),
                (
                    "purchaseQuantity",
                    models.FloatField(null=True, verbose_name="進貨數量(件)"),
                ),
                (
                    "exportQuantity",
                    models.FloatField(null=True, verbose_name="出貨數量(件)"),
                ),
                (
                    "status",
                    models.CharField(max_length=500, verbose_name="調貨狀況or進出貨資訊"),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Goods",
            fields=[
                (
                    "productId",
                    models.CharField(
                        max_length=100,
                        primary_key=True,
                        serialize=False,
                        unique=True,
                        verbose_name="產品ID",
                    ),
                ),
                ("productName", models.CharField(max_length=100, verbose_name="產品名稱")),
                ("position", models.CharField(max_length=50, verbose_name="儲位")),
                ("series", models.CharField(max_length=30, verbose_name="系列")),
                ("quantity", models.IntegerField(verbose_name="入數")),
                (
                    "dailystatus",
                    models.CharField(max_length=500, verbose_name="庫存資訊&調貨狀況"),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Login",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("userName", models.CharField(max_length=15, verbose_name="帳號")),
                ("password", models.CharField(max_length=20, verbose_name="密碼")),
                (
                    "level",
                    models.CharField(
                        choices=[("admin", "Admin"), ("user", "User")],
                        default="user",
                        max_length=10,
                        verbose_name="階級",
                    ),
                ),
                ("Name", models.CharField(max_length=20, verbose_name="用戶名稱")),
            ],
        ),
        migrations.CreateModel(
            name="Transfer",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("productId", models.CharField(max_length=100, verbose_name="產品ID")),
                ("productName", models.CharField(max_length=100, verbose_name="產品名稱")),
                ("position1", models.CharField(max_length=10, verbose_name="儲位1")),
                (
                    "position2",
                    models.CharField(max_length=10, null=True, verbose_name="儲位2"),
                ),
                (
                    "position3",
                    models.CharField(max_length=10, null=True, verbose_name="儲位3"),
                ),
                ("quantity", models.FloatField(verbose_name="數量")),
                (
                    "reason",
                    models.CharField(max_length=500, null=True, verbose_name="未調貨原因"),
                ),
            ],
        ),
    ]