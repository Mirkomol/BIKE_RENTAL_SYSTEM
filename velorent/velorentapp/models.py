from django.db import models


class Hour(models.Model):
    price = models.CharField(null=True, blank=True, max_length=200)
    description = models.TextField('Hour')

    def __str__(self):
        return self.description


class Day(models.Model):
    price = models.CharField(null=True, blank=True,max_length=200)
    description = models.TextField('Day')

    def __str__(self):
        return self.description


class Week(models.Model):
    price = models.CharField(null=True, blank=True, max_length=200)
    description = models.TextField('Week')

    def __str__(self):
        return self.description


class Economy(models.Model):
    img = models.ImageField(blank=True, null=True, default='default.jpg', upload_to='Economy')


class Standard(models.Model):
    img = models.ImageField(blank=True, null=True, default='default.jpg', upload_to='Standard')


class Lux(models.Model):
    img = models.ImageField(blank=True, null=True, default='default.jpg', upload_to='Lux')



class BikeEconomy(models.Model):
    img = models.ImageField(blank=True, null=True, default='default.jpg', upload_to='BikeEconomy')


class BikeStandard(models.Model):
    img = models.ImageField(blank=True, null=True, default='default.jpg', upload_to='BikeStandard')


class BikeLux(models.Model):
    img = models.ImageField(blank=True, null=True, default='default.jpg', upload_to='BikeLux')


