# Generated by Django 4.2.7 on 2023-11-03 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("myapp", "0003_alter_dailyinout_countquantity_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="dailyinout",
            name="goodsInOut",
            field=models.CharField(
                blank=True, max_length=500, null=True, verbose_name="貨品進出狀況"
            ),
        ),
    ]
