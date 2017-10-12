from django.core.urlresolvers import reverse
from django.views.generic import (
    DetailView, ListView, RedirectView,
    UpdateView, CreateView, DeleteView
)
from django.contrib.auth.mixins import LoginRequiredMixin

from intranet_sm.vehiculos_app.models import Asignacion


class AsignacionListView(LoginRequiredMixin, ListView):

    model = Asignacion
    template_name = 'vehiculos_app/asignaciones/asignaciones_list.html'
    context_object_name = 'asignaciones_list'

    page = {
        'title': 'Administrador',
        'subtitle': 'Asignaciones'
    }

    def get_context_data(self, **kwargs):
        context = super(AsignacionListView, self).get_context_data(**kwargs)
        context['page'] = self.page
        return context


class AsignacionCreateView(LoginRequiredMixin, CreateView):

    fields = [
        'asignacion',
    ]

    model = Asignacion
    template_name = 'vehiculos_app/asignaciones/asignaciones_form.html'

    page = {
        'title': 'Administrador',
        'subtitle': 'Datos de la Asignacion'
    }

    def get_context_data(self, **kwargs):
        context = super(AsignacionCreateView, self).get_context_data(**kwargs)
        context['page'] = self.page
        return context

    # send the user back to their own page after a successful update
    def get_success_url(self):
        return reverse('administrator:asignaciones_list')


class AsignacionDetailView(LoginRequiredMixin, DetailView):

    fields = [
        'asignacion',
    ]

    model = Asignacion
    template_name = 'vehiculos_app/asignaciones/asignaciones_detail.html'

    page = {
        'title': 'Administrador',
        'subtitle': 'Detalles de la Asignacion'
    }

    def get_context_data(self, **kwargs):
        context = super(AsignacionDetailView, self).get_context_data(**kwargs)
        context['page'] = self.page
        return context


class AsignacionUpdateView(LoginRequiredMixin, UpdateView):

    fields = [
        'asignacion',
    ]

    model = Asignacion
    template_name = 'vehiculos_app/asignaciones/asignaciones_form.html'

    page = {
        'title': 'Administrador',
        'subtitle': 'Edicion de los datos de la asignacion'
    }

    def get_context_data(self, **kwargs):
        context = super(AsignacionUpdateView, self).get_context_data(**kwargs)
        context['page'] = self.page
        return context

    # send the user back to their own page after a successful update
    def get_success_url(self):
        return reverse('administrator:asignaciones_list')


class AsignacionDeleteView(LoginRequiredMixin, DeleteView):

    fields = [
        'asignacion',
    ]

    model = Asignacion
    template_name = 'vehiculos_app/asignaciones/asignaciones_confirm_delete.html'

    page = {
        'title': 'Administrador',
        'subtitle': 'Eliminacion de la Asignacion'
    }

    def get_context_data(self, **kwargs):
        context = super(AsignacionDeleteView, self).get_context_data(**kwargs)
        context['page'] = self.page
        return context

    # send the user back to their own page after a successful update
    def get_success_url(self):
        return reverse('administrator:asignaciones_list')
