# Generated by Django 3.2.4 on 2021-06-30 15:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Stores', '0013_rename_ip_userview_ip'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='stores',
            name='views',
        ),
        migrations.DeleteModel(
            name='userview',
        ),
    ]
