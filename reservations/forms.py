from django import forms
from.models import Reservation, Timeslot

class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['time_slot','number_of_people']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['time_slot'].queryset = Timeslot.objects.filter(available=True)
        