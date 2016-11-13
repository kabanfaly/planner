from django.db import models


class PublicHoliday(models.Model):

    day = models.DateField(verbose_name="Public holiday date")
    description = models.TextField(null=True)

    def __str__(self):
        return print("Day: {}\n Description: {}", self.day, self.description)
