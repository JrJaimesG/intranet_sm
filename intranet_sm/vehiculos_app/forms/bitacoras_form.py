from django import forms
from functools import partial
from intranet_sm.vehiculos_app.models import Bitacora

TimeInput = partial(forms.TimeInput, {'class': 'TimePickerWidget'})

class BitacoraForm(forms.ModelForm):
    
    class Meta:
         model = Bitacora
         fields = ['hora', 'nivel_tanque_gasolina', 'kilometraje', 'observaciones']

         widgets = {
            'hora': forms.TimeInput(attrs={'type': 'time'}),
        }