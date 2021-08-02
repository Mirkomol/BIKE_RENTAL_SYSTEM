# Generated by Django 3.2.5 on 2021-07-31 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('velorentapp', '0004_auto_20210731_1347'),
    ]

    operations = [
        migrations.CreateModel(
            name='Economy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(blank=True, default='default.jpg', null=True, upload_to='Economy')),
            ],
        ),
        migrations.CreateModel(
            name='Lux',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(blank=True, default='default.jpg', null=True, upload_to='Lux')),
            ],
        ),
        migrations.CreateModel(
            name='Standard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(blank=True, default='default.jpg', null=True, upload_to='Standard')),
            ],
        ),
    ]