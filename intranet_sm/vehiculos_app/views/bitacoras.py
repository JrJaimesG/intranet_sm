from django.core.urlresolvers import reverse
from django.views.generic import (
    DetailView, ListView, RedirectView,
    UpdateView, CreateView, DeleteView
)
from django.contrib.auth.mixins import LoginRequiredMixin

from intranet_sm.vehiculos_app.models import Bitacora, Asignacion, Solicitud
from intranet_sm.vehiculos_app.forms.bitacoras_form import BitacoraForm

class BitacoraListView(LoginRequiredMixin, ListView):

    model = Bitacora
    template_name = 'vehiculos_app/bitacoras/bitacoras_list.html'
    context_object_name = 'bitacoras_list'

    page = {
        'title': 'Administrador',
        'subtitle': 'Bitacoras'
    }

    def get_context_data(self, **kwargs):
        context = super(BitacoraListView, self).get_context_data(**kwargs)
        context['page'] = self.page
        return context


class BitacoraCreateView(LoginRequiredMixin, CreateView):

    model = Bitacora
    form_class = BitacoraForm
    template_name = 'vehiculos_app/bitacoras/bitacoras_form.html'

    page = {
        'title': 'Administrador',
        'subtitle': 'Datos de la Bitacora'
    }

    def get_context_data(self, **kwargs):
        context = super(BitacoraCreateView, self).get_context_data(**kwargs)
        context['page'] = self.page
        context['solicitud'] = Solicitud.objects.get(pk=self.kwargs['solicitud_id'])
        context['asignacion'] = Asignacion.objects.get(pk=self.kwargs['asignacion_id'])
        return context

    # send the user back to their own page after a successful update
    def get_success_url(self):
        return reverse('vehiculosapp:solicitudes_list')

    def form_valid(self, form):
        self.object = form.save(commit=False)
        solicitud = Solicitud.objects.get(pk=self.kwargs['solicitud_id'])
        asignacion = Asignacion.objects.get(pk=self.kwargs['asignacion_id'])
        self.object.solicitud_id = self.kwargs['solicitud_id']
        self.object.asignacion_id = self.kwargs['asignacion_id']
        solicitud.estado_solicitud = "E"
        solicitud.save()
        self.object.save()

        return super(BitacoraCreateView, self).form_valid(form)


class BitacoraDetailView(LoginRequiredMixin, DetailView):

    fields = [
        'hora',
        'nivel_tanque_gasolina',
        'kilometraje',
        'observaciones',
        'entrada_salida',
        'fecha_reg',
        'fecha_act',
    ]

    model = Bitacora
    template_name = 'vehiculos_app/bitacoras/bitacoras_detail.html'

    page = {
        'title': 'Administrador',
        'subtitle': 'Detalles de la Bitacora'
    }

    def get_context_data(self, **kwargs):
        context = super(BitacoraDetailView, self).get_context_data(**kwargs)
        context['page'] = self.page     
        return context


class BitacoraUpdateView(LoginRequiredMixin, UpdateView):

    fields = [
        'hora',
        'nivel_tanque_gasolina',
        'kilometraje',
        'observaciones',
        'entrada_salida',
    ]

    model = Bitacora
    template_name = 'vehiculos_app/bitacoras/bitacoras_form.html'

    page = {
        'title': 'Administrador',
        'subtitle': 'Edicion de los datos de la bitacora'
    }

    def get_context_data(self, **kwargs):
        context = super(BitacoraUpdateView, self).get_context_data(**kwargs)
        context['page'] = self.page
        context['solicitud'] = Solicitud.objects.get(pk=self.kwargs['solicitud_id'])
        context['asignacion'] = Asignacion.objects.get(pk=self.kwargs['asignacion_id'])
        return context

    # send the user back to their own page after a successful update
    def get_success_url(self):
        return reverse('vehiculosapp:solicitudes_view', kwargs={"pk": self.kwargs['solicitud_id']})

    def form_valid(self, form):
        self.object = form.save(commit=False)
        solicitud = Solicitud.objects.get(pk=self.kwargs['solicitud_id'])
        self.object.solicitud_id = self.kwargs['solicitud_id']
        self.object.asignacion_id = self.kwargs['asignacion_id']
        if solicitud.estado_solicitud == "E":
           solicitud.estado_solicitud = "F" 
           solicitud.save()
           self.object.entrada_salida = "E"
           self.object.save()

        return super(BitacoraUpdateView, self).form_valid(form)


class BitacoraDeleteView(LoginRequiredMixin, DeleteView):

    fields = [
        'hora',
        'nivel_tanque_gasolina',
        'kilometraje',
        'observaciones',
        'entrada_salida',
        'fecha_reg',
        'fecha_act',
    ]

    model = Bitacora
    template_name = 'vehiculos_app/bitacoras/bitacoras_confirm_delete.html'

    page = {
        'title': 'Administrador',
        'subtitle': 'Eliminacion de la Bitacora'
    }

    def get_context_data(self, **kwargs):
        context = super(BitacoraDeleteView, self).get_context_data(**kwargs)
        context['page'] = self.page
        context['solicitud'] = Solicitud.objects.get(pk=self.kwargs['solicitud_id'])
        context['asignacion'] = Asignacion.objects.get(pk=self.kwargs['asignacion_id'])
        return context

    # send the user back to their own page after a successful update
    def get_success_url(self):
        return reverse('vehiculosapp:solicitudes_list')
