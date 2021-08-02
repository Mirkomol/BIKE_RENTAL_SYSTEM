# Generated by Django 3.2.5 on 2021-07-31 08:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('velorentapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='day',
            name='price',
            field=models.IntegerField(blank=True, null=True, verbose_name='Day'),
        ),
        migrations.AlterField(
            model_name='hour',
            name='price',
            field=models.IntegerField(blank=True, null=True, verbose_name='Hour'),
        ),
        migrations.AlterField(
            model_name='week',
            name='price',
            field=models.IntegerField(blank=True, null=True, verbose_name='Week'),
        ),
    ]
