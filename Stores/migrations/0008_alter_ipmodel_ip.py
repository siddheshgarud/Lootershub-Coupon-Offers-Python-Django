# Generated by Django 3.2.4 on 2021-08-03 20:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Stores', '0007_alter_offers_ourl'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ipmodel',
            name='ip',
            field=models.TextField(max_length=100),
        ),
    ]
