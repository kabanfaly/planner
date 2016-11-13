from django.db import models
from city import models as city


class Workplace(models.Model):

    name = models.CharField(max_length=45)
    address = models.TextField(null=True)
    zip_code = models.CharField(max_length=45, null=True)
    city_name = models.CharField(max_length=45, null=True)
    country = models.CharField(max_length=45, null=True)
    phone = models.CharField(max_length=45, null=True)
    city = models.ForeignKey(city.City)

    def __str__(self):
        return print("{} \n {},  {} {} {}".format(self.name, self.address, self.zip_code, self.city_name, self.country))


