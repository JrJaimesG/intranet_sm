from django import forms
from functools import partial
from intranet_sm.vehiculos_app.models import Solicitud

DateInput = partial(forms.DateInput, {'class': 'datepicker'})


class SolicitudForm(forms.ModelForm):
    
    class Meta:
         model = Solicitud
         fields = ['actividad_a_realizar', 'destino', 'salida_fecha', 'salida_hora', 'llegada_fecha', 
                    'llegada_hora', 'n_ocupantes', 'carretera', 'carga', 'observaciones']

         widgets = {
            'salida_fecha': forms.DateInput(format=('%d/%m/%Y'), attrs={'class': 'datepicker', 'placeholder': 'Seleccione una fecha'}),
            'salida_hora': forms.TimeInput(format=('%I:%M %p'), attrs={'type': 'time'}),
            'llegada_fecha': forms.DateInput(format=('%d/%m/%Y'), attrs={'class': 'datepicker', 'placeholder': 'Seleccione una fecha'}),
            'llegada_hora': forms.TimeInput(attrs={'type': 'time'}),
        }