from django.core.urlresolvers import reverse
from django.views.generic import (
    DetailView, ListView, RedirectView,
    UpdateView, CreateView, DeleteView
)
from django.contrib.auth.mixins import LoginRequiredMixin

from intranet_sm.vehiculos_app.models import Chofer


class ChoferListView(LoginRequiredMixin, ListView):

    model = Chofer
    template_name = 'vehiculos_app/choferes/choferes_list.html'
    context_object_name = 'choferes_list'

    page = {
        'title': 'Administrador',
        'subtitle': 'Choferes'
    }

    def get_context_data(self, **kwargs):
        context = super(ChoferListView, self).get_context_data(**kwargs)
        context['page'] = self.page
        return context


class ChoferCreateView(LoginRequiredMixin, CreateView):

    fields = [
        'chofer',
    ]

    model = Chofer
    template_name = 'vehiculos_app/choferes/choferes_form.html'

    page = {
        'title': 'Administrador',
        'subtitle': 'Datos del Chofer'
    }

    def get_context_data(self, **kwargs):
        context = super(ChoferCreateView, self).get_context_data(**kwargs)
        context['page'] = self.page
        return context

    # send the user back to their own page after a successful update
    def get_success_url(self):
        return reverse('administrator:choferes_list')


class ChoferDetailView(LoginRequiredMixin, DetailView):

    fields = [
        'chofer',
    ]

    model = Chofer
    template_name = 'vehiculos_app/choferes/choferes_detail.html'

    page = {
        'title': 'Administrador',
        'subtitle': 'Detalles del Chofer'
    }

    def get_context_data(self, **kwargs):
        context = super(ChoferDetailView, self).get_context_data(**kwargs)
        context['page'] = self.page
        return context


class ChoferUpdateView(LoginRequiredMixin, UpdateView):

    fields = [
        'chofer',
    ]

    model = Chofer
    template_name = 'vehiculos_app/choferes/choferes_form.html'

    page = {
        'title': 'Administrador',
        'subtitle': 'Edicion de los datos del chofer'
    }

    def get_context_data(self, **kwargs):
        context = super(ChoferUpdateView, self).get_context_data(**kwargs)
        context['page'] = self.page
        return context

    # send the user back to their own page after a successful update
    def get_success_url(self):
        return reverse('administrator:choferes_list')


class ChoferDeleteView(LoginRequiredMixin, DeleteView):

    fields = [
        'chofer',
    ]

    model = Chofer
    template_name = 'vehiculos_app/choferes/choferes_confirm_delete.html'

    page = {
        'title': 'Administrador',
        'subtitle': 'Eliminacion del Chofer'
    }

    def get_context_data(self, **kwargs):
        context = super(ChoferDeleteView, self).get_context_data(**kwargs)
        context['page'] = self.page
        return context

    # send the user back to their own page after a successful update
    def get_success_url(self):
        return reverse('administrator:choferes_list')
