# Generated by Django 3.2.5 on 2021-08-04 07:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Stores', '0013_remove_coupon_cverifed'),
    ]

    operations = [
        migrations.AddField(
            model_name='coupon',
            name='cverify',
            field=models.BooleanField(default=True),
        ),
    ]