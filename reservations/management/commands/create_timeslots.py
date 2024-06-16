import datetime
from django.core.management.base import BaseCommand
from reservations.models import Timeslot

class Command(BaseCommand):
    help = 'Create TimeSlots for the next 30 days'

    def handle(self, *args, **kwargs):
        start_date = datetime.date.today()
        end_date = start_date + datetime.timedelta(days=30)
        start_time = datetime.time(hour=10, minute=0)
        end_time = datetime.time(hour=21, minute=0)
        delta = datetime.timedelta(days=1)

        while start_date <= end_date:
            Timeslot.objects.create(date=start_date, start_time=start_time, end_time=end_time, available=True)
            start_date += delta

        self.stdout.write(self.style.SUCCESS('Successfully created timeslots for the next 30 days'))
