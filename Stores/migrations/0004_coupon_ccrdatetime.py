# Generated by Django 3.2.4 on 2021-07-06 19:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Stores', '0003_auto_20210705_0151'),
    ]

    operations = [
        migrations.AddField(
            model_name='coupon',
            name='ccrdatetime',
            field=models.DateTimeField(blank=True, null=True),
        ),
        
    ]
