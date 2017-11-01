from django.core.urlresolvers import reverse
from django.views.generic import (
    DetailView, ListView, RedirectView,
    UpdateView, CreateView, DeleteView
)
from django.contrib.auth.mixins import LoginRequiredMixin
from braces.views import GroupRequiredMixin
from intranet_sm.vehiculos_app.models import Vehiculo


class VehiculoListView(GroupRequiredMixin, ListView):

    #required
    group_required = u'Transporte'
    raise_exception = True

    model = Vehiculo
    template_name = 'vehiculos_app/vehiculos/vehiculos_list.html'
    context_object_name = 'vehiculos_list'

    page = {
        'title': 'Administrador',
        'subtitle': 'Vehiculos'
    }

    def get_context_data(self, **kwargs):
        context = super(VehiculoListView, self).get_context_data(**kwargs)
        context['page'] = self.page
        return context


class VehiculoCreateView(LoginRequiredMixin, CreateView):

    fields = [
        'placa',
        'marca',
        'modelo',
        'color',
        'tipo',
        'uso',
        'n_puestos',
        'kilometraje',
    ]

    model = Vehiculo
    template_name = 'vehiculos_app/vehiculos/vehiculos_form.html'

    page = {
        'title': 'Administrador',
        'subtitle': 'Datos del Vehiculo'
    }

    def get_context_data(self, **kwargs):
        context = super(VehiculoCreateView, self).get_context_data(**kwargs)
        context['page'] = self.page
        return context

    # send the user back to their own page after a successful update
    def get_success_url(self):
        return reverse('vehiculosapp:vehiculos_list')


class VehiculoDetailView(LoginRequiredMixin, DetailView):

    fields = [
        'placa',
        'marca',
        'modelo',
        'color',
        'tipo',
        'uso',
        'n_puestos',
        'capa_tanque_gasolina',
    ]

    model = Vehiculo
    template_name = 'vehiculos_app/vehiculos/vehiculos_detail.html'

    page = {
        'title': 'Administrador',
        'subtitle': 'Detalles del Vehiculo'
    }

    def get_context_data(self, **kwargs):
        context = super(VehiculoDetailView, self).get_context_data(**kwargs)
        context['page'] = self.page
        return context


class VehiculoUpdateView(LoginRequiredMixin, UpdateView):

    fields = [
        'placa',
        'marca',
        'modelo',
        'color',
        'tipo',
        'uso',
        'n_puestos',
        'capa_tanque_gasolina',
    ]

    model = Vehiculo
    template_name = 'vehiculos_app/vehiculos/vehiculos_form.html'

    page = {
        'title': 'Administrador',
        'subtitle': 'Edicion de los datos del vehiculo'
    }

    def get_context_data(self, **kwargs):
        context = super(VehiculoUpdateView, self).get_context_data(**kwargs)
        context['page'] = self.page
        return context

    # send the user back to their own page after a successful update
    def get_success_url(self):
        return reverse('vehiculosapp:vehiculos_list')


class VehiculoDeleteView(LoginRequiredMixin, DeleteView):

    fields = [
        'placa',
        'marca',
        'modelo',
        'color',
        'tipo',
        'uso',
        'n_puestos',
        'capa_tanque_gasolina',
    ]

    model = Vehiculo
    template_name = 'vehiculos_app/vehiculos/vehiculos_confirm_delete.html'

    page = {
        'title': 'Administrador',
        'subtitle': 'Eliminacion del Vehiculo'
    }

    def get_context_data(self, **kwargs):
        context = super(VehiculoDeleteView, self).get_context_data(**kwargs)
        context['page'] = self.page
        return context

    # send the user back to their own page after a successful update
    def get_success_url(self):
        return reverse('vehiculosapp:vehiculos_list')
