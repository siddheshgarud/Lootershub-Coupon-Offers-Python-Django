# Generated by Django 3.2.4 on 2021-06-23 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Stores', '0005_auto_20210623_2122'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coupon',
            name='ccredatetime',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='coupon',
            name='cexpdatetime',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
