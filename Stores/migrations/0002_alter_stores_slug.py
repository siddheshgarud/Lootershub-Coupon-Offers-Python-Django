# Generated by Django 3.2.4 on 2021-07-04 19:39

import Stores.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Stores', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stores',
            name='slug',
            field=models.CharField(default=Stores.models.randomString, max_length=25, unique=True),
        ),
    ]
