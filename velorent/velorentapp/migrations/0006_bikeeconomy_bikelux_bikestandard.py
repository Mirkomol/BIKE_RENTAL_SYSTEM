# Generated by Django 3.2.5 on 2021-07-31 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('velorentapp', '0005_economy_lux_standard'),
    ]

    operations = [
        migrations.CreateModel(
            name='BikeEconomy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(blank=True, default='default.jpg', null=True, upload_to='BikeEconomy')),
            ],
        ),
        migrations.CreateModel(
            name='BikeLux',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(blank=True, default='default.jpg', null=True, upload_to='BikeLux')),
            ],
        ),
        migrations.CreateModel(
            name='BikeStandard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(blank=True, default='default.jpg', null=True, upload_to='BikeStandard')),
            ],
        ),
    ]
