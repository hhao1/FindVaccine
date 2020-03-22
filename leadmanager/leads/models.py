from django.db import models


class Vaccine (models.Model):
    name = models.CharField(max_length=100)
    detail = models.CharField(max_length=10000, blank=True)
    notice = models.CharField(max_length=10000, blank=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class Lead(models.Model):
    Country_Name = models.CharField(max_length=100)
    Vaccines = models.ManyToManyField(Vaccine)

    class Meta:
        ordering = ["Country_Name"]

    def __str__(self):
        return self.Country_Name


class Makers(models.Model):
    name = models.CharField(max_length=100)
    lon = models.DecimalField(max_digits=22, decimal_places=16)
    lat = models.DecimalField(max_digits=22, decimal_places=16)
    phone = models.CharField(max_length=12, default=None, null=True)
    hours = models.CharField(max_length=20, default=None, null=True)
    address = models.CharField(max_length=100, default=None, null=True)
    injection_certified = models.BooleanField(default=True)
    certified_travel_consultant = models.BooleanField(default=True)
    additional_prescribing_authority = models.BooleanField(default=True)
    others = models.CharField(max_length=1000, default=None, null=True)
