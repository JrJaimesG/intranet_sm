from django.core.urlresolvers import reverse
from django.views.generic import (
    DetailView, ListView, RedirectView,
    UpdateView, CreateView, DeleteView
)
from django.contrib.auth.mixins import LoginRequiredMixin

from intranet_sm.vehiculos_app.models import Asignacion, Solicitud


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
        'vehiculo',
        'chofer',
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
        context['solicitud'] = Solicitud.objects.get(pk=self.kwargs['pk'])
        return context

    # send the user back to their own page after a successful update
    def get_success_url(self):
        #return reverse('vehiculosapp:solicitudes_view', kwargs={"pk": self.kwargs['solicitud_id']})
        return reverse('vehiculosapp:solicitudes_view', kwargs={"pk": self.kwargs['solicitud_id']})

    def form_valid(self, form):
        self.object = form.save(commit=False)
        solicitud = Solicitud.objects.get(pk=self.kwargs['pk'])
        self.object.solicitud_id = self.kwargs['pk']
        solicitud.estado_solicitud = "A"
        solicitud.save()
        self.object.save()

        return super(AsignacionCreateView, self).form_valid(form)


class AsignacionDetailView(LoginRequiredMixin, DetailView):

    fields = [
        'vehiculo',
        'chofer',
        'fecha_reg',
        'fecha_act',
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
        'vehiculo',
        'chofer',
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
        context['solicitud'] = Solicitud.objects.get(pk=self.kwargs['solicitud_id'])
        return context

    # send the user back to their own page after a successful update
    def get_success_url(self):
        return reverse('vehiculosapp:solicitudes_view', kwargs={"pk": self.kwargs['solicitud_id']})


class AsignacionDeleteView(LoginRequiredMixin, DeleteView):

    fields = [
        'vehiculo',
        'chofer',
        'fecha_reg',
        'fecha_act',
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
        context['solicitud'] = Solicitud.objects.get(pk=self.kwargs['solicitud_id'])
        return context

    def form_valid(self, form):
        self.object = form.save(commit=False)
        solicitud = Solicitud.objects.get(pk=self.kwargs['solicitud_id'])
        print ("estado_solicitud: ", solicitud.estado_solicitud)
        self.object.solicitud_id = self.kwargs['pk']
        if solicitud.estado_solicitud == 'A':
            solicitud.estado_solicitud = 'N'
            solicitud.save()
        self.object.save()
        print ("estado_solicitud: despues ", solicitud.estado_solicitud)

    # send the user back to their own page after a successful update
    def get_success_url(self):
        return reverse('vehiculosapp:solicitudes_view', kwargs={"pk": self.kwargs['solicitud_id']})
