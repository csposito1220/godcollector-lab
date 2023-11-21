from django.forms import ModelForm
from .models import Prayer

class PrayerForm(ModelForm):
    class Meta:
        model = Prayer
        fields = ['date', 'prayer']