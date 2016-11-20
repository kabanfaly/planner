from django.db import models
from employee.models import Employee
from workplace.models import Workplace


class Schedule(models.Model):
    start_time = models.DateTimeField(verbose_name="Work start time")
    end_time = models.DateTimeField(verbose_name="Work end time")
    break_time = models.TimeField(null=True)
    day_hours = models.TimeField(verbose_name="Number of hours worked as day hours", null=True)
    night_hours = models.TimeField(verbose_name="Number of hours worked as night hours", null=True)
    sunday_day_hours = models.TimeField(verbose_name="Sunday: Number of hours worked as day hours", null=True)
    sunday_night_hours = models.TimeField(verbose_name="Sunday: Number of hours worked as night hours", null=True)
    public_holiday_day_hours = models.TimeField(verbose_name="Public holiday: Number of hours worked as day hours", null=True)
    public_holiday_night_hours = models.TimeField(verbose_name="Public holiday: Number of hours worked as night hours", null=True)
    employee = models.ForeignKey(Employee)
    workplace = models.ForeignKey(Workplace)

    def __str__(self):
        print("{}\nWorkplace: {}\nStart time: {}\nEnd time: {}\nBreak: {}\nDay hours: {}\nNight hours: {}"
              .format(self.employee, self.workplace, self.start_time, self.end_time,
                      self.break_time, self.day_hours, self.night_hours))