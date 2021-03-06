# Generated by Django 3.2.4 on 2021-08-04 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0002_alter_banner_bimage'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dealotd',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dealcompany', models.CharField(max_length=50)),
                ('dealname', models.CharField(max_length=100)),
                ('dealtag', models.CharField(max_length=50)),
                ('dealtime', models.DateTimeField()),
                ('dealurl', models.URLField()),
                ('dealimage', models.ImageField(default='', upload_to='Home/')),
            ],
        ),
    ]
