from django.conf.urls import url

from intranet_sm.vehiculos_app.views import solicitudes, vehiculos, choferes, asignaciones, bitacoras

urlpatterns = [
    #Solicitudes

    url(
        regex=r'^solicitud/$',
        view=solicitudes.SolicitudListView.as_view(),
        name='solicitudes_list'
    ),
    url(
        regex=r'^solicitud/admin/$',
        view=solicitudes.SolicitudListAdminView.as_view(),
        name='solicitudes_list_admin'
    ),
    url(
        regex=r'^solicitud/create/$',
        view=solicitudes.SolicitudCreateView.as_view(),
        name='solicitudes_create'
    ),

    url(
        regex=r'^solicitud/view/(?P<pk>\d+)$',
        view=solicitudes.SolicitudDetailView.as_view(),
        name='solicitudes_view'
    ),

    url(
        regex=r'^solicitud/update/(?P<pk>\d+)$',
        view=solicitudes.SolicitudUpdateView.as_view(),
        name='solicitudes_update'
    ),

    url(
        regex=r'^solicitud/delete/(?P<pk>\d+)$',
        view=solicitudes.SolicitudDeleteView.as_view(),
        name='solicitudes_delete'
    ),
    url(
        regex=r'^solicitud/anular/(?P<pk>\d+)$',
        view=solicitudes.SolicitudAnularView.as_view(),
        name='solicitudes_anular'
    ),

    #Vehiculos

    url(
        regex=r'^vehiculo/$',
        view=vehiculos.VehiculoListView.as_view(),
        name='vehiculos_list'
    ),
    url(
        regex=r'^vehiculo/create/$',
        view=vehiculos.VehiculoCreateView.as_view(),
        name='vehiculos_create'
    ),

    url(
        regex=r'^vehiculo/view/(?P<pk>\d+)$',
        view=vehiculos.VehiculoDetailView.as_view(),
        name='vehiculos_view'
    ),

    url(
        regex=r'^vehiculo/update/(?P<pk>\d+)$',
        view=vehiculos.VehiculoUpdateView.as_view(),
        name='vehiculos_update'
    ),

    url(
        regex=r'^vehiculo/delete/(?P<pk>\d+)$',
        view=vehiculos.VehiculoDeleteView.as_view(),
        name='vehiculos_delete'
    ),

    #Choferes

    url(
        regex=r'^chofer/$',
        view=choferes.ChoferListView.as_view(),
        name='choferes_list'
    ),
    url(
        regex=r'^chofer/create/$',
        view=choferes.ChoferCreateView.as_view(),
        name='choferes_create'
    ),

    url(
        regex=r'^chofer/view/(?P<pk>\d+)$',
        view=choferes.ChoferDetailView.as_view(),
        name='choferes_view'
    ),

    url(
        regex=r'^solicitud/update/(?P<pk>\d+)$',
        view=choferes.ChoferUpdateView.as_view(),
        name='choferes_update'
    ),

    url(
        regex=r'^chofer/delete/(?P<pk>\d+)$',
        view=choferes.ChoferDeleteView.as_view(),
        name='choferes_delete'
    ),

    #Asignaciones

    url(
        regex=r'^asignacion/$',
        view=asignaciones.AsignacionListView.as_view(),
        name='asignaciones_list'
    ),
    url(
        regex=r'^asignacion/create/(?P<solicitud_id>\d+)/$',
        view=asignaciones.AsignacionCreateView.as_view(),
        name='asignaciones_create'
    ),

    url(
        regex=r'^asignacion/view/(?P<pk>\d+)$',
        view=asignaciones.AsignacionDetailView.as_view(),
        name='asignaciones_view'
    ),

    url(
        regex=r'^asignacion/update/(?P<solicitud_id>\d+)/(?P<pk>\d+)$',
        view=asignaciones.AsignacionUpdateView.as_view(),
        name='asignaciones_update'
    ),

    url(
        regex=r'^asignacion/delete/(?P<solicitud_id>\d+)/(?P<pk>\d+)$',
        view=asignaciones.AsignacionDeleteView.as_view(),
        name='asignaciones_delete'
    ),

    #Bitacoras

    url(
        regex=r'^bitacora/$',
        view=bitacoras.BitacoraListView.as_view(),
        name='bitacoras_list'
    ),
    url(
        regex=r'^bitacora/create/(?P<solicitud_id>\d+)/(?P<asignacion_id>\d+)/$',
        view=bitacoras.BitacoraCreateView.as_view(),
        name='bitacoras_create'
    ),

    url(
        regex=r'^bitacora/view/(?P<pk>\d+)$',
        view=bitacoras.BitacoraDetailView.as_view(),
        name='bitacoras_view'
    ),

    url(
        regex=r'^bitacora/update/(?P<solicitud_id>\d+)/(?P<asignacion_id>\d+)/(?P<pk>\d+)$',
        view=bitacoras.BitacoraUpdateView.as_view(),
        name='bitacoras_update'
    ),

    url(
        regex=r'^bitacora/delete/(?P<solicitud_id>\d+)/(?P<asignacion_id>\d+)/(?P<pk>\d+)$',
        view=bitacoras.BitacoraDeleteView.as_view(),
        name='bitacoras_delete'
    ),

]
