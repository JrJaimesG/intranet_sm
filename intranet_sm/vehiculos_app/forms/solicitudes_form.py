from django import forms
from functools import partial
from intranet_sm.vehiculos_app.models import Solicitud

DateInput = partial(forms.DateInput, {'class': 'datepicker'})
TimeInput = partial(forms.TimeInput, {'class': 'timepicker'})

'''
class TimePickerWidget(forms.TimeInput):                                                  
    def render(self, name, value, attrs=None):                                                
        htmlString = u''                                                                      
        htmlString += u'<select name="%s">' % (name)                                          
        for i in range(12):                                                                   
                htmlString += ('<option value="%d:00 AM">%d:00 AM</option>' % (i,i))          
        htmlString +='</select>'                                                              
        return mark_safe(u''.join(htmlString))
        ''' 

class SolicitudForm(forms.ModelForm):
    
    class Meta:
         model = Solicitud
         fields = ['actividad_a_realizar', 'destino', 'salida_fecha', 'salida_hora', 'llegada_fecha', 
                    'llegada_hora', 'n_ocupantes', 'carretera', 'carga', 'observaciones']

         widgets = {
            'salida_fecha': forms.DateInput(format=('%d/%m/%Y'), attrs={'class': 'datepicker', 'placeholder': 'Seleccione una fecha'}),
            #'salida_hora': forms.TimeField(format=('%I:%M %p'), widget=TimePickerWidget(format='%I:%M %p')),
            #'salida_hora': forms.TimeInput(format=('%I:%M %p'), attrs={'class': 'timepicker'}),
            'llegada_fecha': forms.DateInput(format=('%d/%m/%Y'), attrs={'class': 'datepicker', 'placeholder': 'Seleccione una fecha'}),
            'llegada_hora': forms.TimeInput(attrs={'class': 'timepicker'}),
        }

'''
from django import forms
from functools import partial
from intranet_sm.report_app.models import Reporte

DateInput = partial(forms.DateInput, {'class': 'datepicker'})


class ReporteForm(forms.ModelForm):

    class Meta:
        model = Reporte
        fields = ['tipo_reporte', 'observador', 'observadores','fecha_obs', 'asistente', 'proyecto',
            'telescopio', 'datos', 'horas_trabajadas', 'hp_clima', 'hp_instrumentos',
            'hp_software', 'vacio_camara', 'vacio_ls', 'vacio_li', 'enviado', 'comentarios']

        widgets = {

            'fecha_obs': forms.DateInput(format=('%d/%m/%Y'), attrs={'class': 'datepicker', 'placeholder': 'Seleccione una fecha'}),
            'comentarios': forms.Textarea(attrs={'placeholder': 'Comentarios'}),
        }
'''