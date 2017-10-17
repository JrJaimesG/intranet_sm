# -*- coding: utf-8 -*-
from django.shortcuts import redirect
from django.core.urlresolvers import reverse
from django.views.generic import (
    DetailView, ListView, RedirectView,
    UpdateView, CreateView, DeleteView
)
from django.contrib.auth.mixins import LoginRequiredMixin

from intranet_sm.vehiculos_app.models import Solicitud
from intranet_sm.vehiculos_app.forms.solicitudes_form import SolicitudForm


class SolicitudListView(LoginRequiredMixin, ListView):

    model = Solicitud
    template_name = 'vehiculos_app/solicitudes/solicitudes_list.html'
    context_object_name = 'solicitudes_list'

    page = {
        'title': 'Administrador',
        'subtitle': 'Solicitudes'
    }

    def get_context_data(self, **kwargs):
        context = super(SolicitudListView, self).get_context_data(**kwargs)
        context['page'] = self.page
        return context


class SolicitudCreateView(LoginRequiredMixin, CreateView):

    model = Solicitud
    form_class = SolicitudForm
    template_name = 'vehiculos_app/solicitudes/solicitudes_form.html'

    page = {
        'title': 'Administrador',
        'subtitle': 'Creación de la Solicitud'
    }

    #success_url = 'vehiculosapp:solicitudes_list'

    def get_context_data(self, **kwargs):
        context = super(SolicitudCreateView, self).get_context_data(**kwargs)
        context['page'] = self.page
        return context

    # send the user back to their own page after a successful update
    def get_success_url(self):
        return reverse('vehiculosapp:solicitudes_list')

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.empleado = self.request.user.id
        self.object.estado_solicitud = "N"
        self.object.save()

        #messages.add_message(self.request,
        #                     messages.SUCCESS, 'Se ha creado la cuenta del empleado')

        #super(SolicitudCreateView, self).form_valid(form)

        #return redirect(self.success_url)
        return super(SolicitudCreateView, self).form_valid(form)


class SolicitudDetailView(LoginRequiredMixin, DetailView):

    fields = [
        'empleado',
        'actividad_a_realizar',
        'destino',
        'salida_fecha',
        'salida_hora',
        'llegada_fecha',
        'llegada_hora',
        'n_ocupantes',
        'carretera',
        'carga',
        'observaciones',
        'estado_solicitud',
        'fecha_reg',
        'fecha_act',
    ]

    model = Solicitud
    template_name = 'vehiculos_app/solicitudes/solicitudes_detail.html'

    page = {
        'title': 'Administrador',
        'subtitle': 'Detalles de la Solicitud'
    }

    def get_context_data(self, **kwargs):
        context = super(SolicitudDetailView, self).get_context_data(**kwargs)
        context['page'] = self.page
        return context


class SolicitudUpdateView(LoginRequiredMixin, UpdateView):

    fields = [
        'empleado',
        'actividad_a_realizar',
        'destino',
        'salida_fecha',
        'salida_hora',
        'llegada_fecha',
        'llegada_hora',
        'n_ocupantes',
        'carretera',
        'carga',
        'observaciones',
        'estado_solicitud',
    ]

    model = Solicitud
    template_name = 'vehiculos_app/solicitudes/solicitudes_form.html'

    page = {
        'title': 'Administrador',
        'subtitle': 'Edición de la Solicitud'
    }

    def get_context_data(self, **kwargs):
        context = super(SolicitudUpdateView, self).get_context_data(**kwargs)
        context['page'] = self.page
        return context

    # send the user back to their own page after a successful update
    def get_success_url(self):
        return reverse('vehiculosapp:solicitudes_list')


class SolicitudDeleteView(LoginRequiredMixin, DeleteView):

    fields = [
        'empleado',
        'actividad_a_realizar',
        'destino',
        'salida_fecha',
        'salida_hora',
        'llegada_fecha',
        'llegada_hora',
        'n_ocupantes',
        'carretera',
        'carga',
        'observaciones',
        'estado_solicitud',
        'fecha_reg',
        'fecha_act',
    ]

    model = Solicitud
    template_name = 'vehiculos_app/solicitudes/solicitudes_confirm_delete.html'

    page = {
        'title': 'Administrador',
        'subtitle': 'Eliminacion de la Solicitud'
    }

    def get_context_data(self, **kwargs):
        context = super(SolicitudDeleteView, self).get_context_data(**kwargs)
        context['page'] = self.page
        return context

    # send the user back to their own page after a successful update
    def get_success_url(self):
        return reverse('vehiculosapp:solicitudes_list')
