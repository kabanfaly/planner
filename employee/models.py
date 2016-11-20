from django.db import models
from city.models import City


class Employee(models.Model):

    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    address = models.TextField(null=True)
    zip_code = models.CharField(max_length=45, null=True)
    city_name = models.CharField(max_length=45, null=True)
    country = models.CharField(max_length=45, null=True)
    phone = models.CharField(max_length=45, null=True)
    birth_date = models.DateField(null=True)
    contract_start_date = models.DateField(verbose_name="Start contract date")
    contract_end_date = models.DateField(verbose_name="End contract date", null=True)
    contract_type = models.CharField(max_length=45)
    id_type = models.CharField(max_length=45, verbose_name="ID card type")
    id_start_date = models.DateField(verbose_name="ID card start date", null=True)
    id_end_date = models.DateField(verbose_name="ID card due date", null=True)
    citizenship = models.CharField(max_length=45)
    email = models.CharField(max_length=100, null=True)
    city = models.ForeignKey(City)


def __str__(self):
    return print("First name: {} \n Last name: {}, Address: {},  {} {} {} "
                 .format(self.first_name, self.last_name, self.address, self.zip_code, self.city_name, self.country))
