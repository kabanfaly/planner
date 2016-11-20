from django.db import models
from city.models import City


class Workplace(models.Model):

    name = models.CharField(max_length=45)
    address = models.TextField(null=True)
    zip_code = models.CharField(max_length=45, null=True)
    city_name = models.CharField(max_length=45, null=True)
    country = models.CharField(max_length=45, null=True)
    phone = models.CharField(max_length=45, null=True)
    city = models.ForeignKey(City)

    def __str__(self):
        return print("{} \n {},  {} {} {}".format(self.name, self.address, self.zip_code, self.city_name, self.country))


