from django.core.urlresolvers import reverse
from django.views.generic import (
    DetailView, ListView, RedirectView,
    UpdateView, CreateView, DeleteView
)
from django.contrib.auth.mixins import LoginRequiredMixin

from intranet_sm.vehiculos_app.models import Bitacora


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

    fields = [
        'asignacion',
        'fecha_hora',
        'nivel_tanque_gasolina',
        'kilometraje',
        'observaciones',
        'entrada_salida',
    ]

    model = Bitacora
    template_name = 'vehiculos_app/bitacoras/bitacoras_form.html'

    page = {
        'title': 'Administrador',
        'subtitle': 'Datos de la Bitacora'
    }

    def get_context_data(self, **kwargs):
        context = super(BitacoraCreateView, self).get_context_data(**kwargs)
        context['page'] = self.page
        return context

    # send the user back to their own page after a successful update
    def get_success_url(self):
        return reverse('vehiculosapp:bitacoras_list')


class BitacoraDetailView(LoginRequiredMixin, DetailView):

    fields = [
        'asignacion',
        'fecha_hora',
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
        'asignacion',
        'fecha_hora',
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
        return context

    # send the user back to their own page after a successful update
    def get_success_url(self):
        return reverse('vehiculosapp:bitacoras_list')


class BitacoraDeleteView(LoginRequiredMixin, DeleteView):

    fields = [
        'asignacion',
        'fecha_hora',
        'nivel_tanque_gasolina',
        'kilometraje',
        'observaciones',
        'entrada_salida',
        'fecha_reg',
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
        return context

    # send the user back to their own page after a successful update
    def get_success_url(self):
        return reverse('vehiculosapp:bitacoras_list')
