# Generated by Django 3.2.4 on 2021-06-30 19:52

import Stores.models
from django.db import migrations, models
import django.db.models.deletion
import django_resized.forms


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='stores',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stores_name', models.CharField(max_length=50)),
                ('slug', models.CharField(default=Stores.models.randomString, max_length=25)),
                ('sdesc', models.CharField(default='', max_length=100)),
                ('simage', models.ImageField(default='', upload_to='Store/images/stores')),
                ('sresimage', django_resized.forms.ResizedImageField(crop=None, default='', force_format=None, keep_meta=True, quality=0, size=[370, 250], upload_to='Store/images/stores')),
                ('scategory', models.CharField(default='', max_length=100)),
                ('ssubcategory', models.CharField(default='', max_length=100)),
                ('sdatetime', models.DateTimeField()),
            ],
            options={
                'ordering': ('-stores_name',),
            },
        ),
        migrations.CreateModel(
            name='coupon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cname', models.CharField(max_length=100)),
                ('cpercentage', models.IntegerField()),
                ('ccategory', models.CharField(max_length=200)),
                ('cfid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Stores.stores')),
            ],
        ),
        
    ]
