# Generated by Django 3.2.5 on 2021-08-04 07:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Stores', '0009_coupon_cdetails'),
    ]

    operations = [
        migrations.AddField(
            model_name='coupon',
            name='cverify',
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
    ]
