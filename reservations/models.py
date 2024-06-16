from django.db import models
from django.conf import settings

# Create your models here.
from django.contrib.auth.models import User

# 時間帯
class Timeslot(models.Model):
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    available = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.date} {self.start_time} - {self.end_time}"
    
# 預約
class Reservation(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    time_slot = models.ForeignKey(Timeslot, on_delete=models.CASCADE)
    number_of_people = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username} {self.time_slot} for {self.number_of_people} people"