# -*- coding: utf-8 -*-

import datetime
from django.db import models
from intranet_sm.users.models import Empleado

CARRETERA_CHOICES = (
    ('P', 'Pavimentada'),
    ('T', 'De Tierra'),
)

CARGA_CHOICES = (
    ('NO', 'No Aplica'),
    ('ME', 'Menor o igual a un metro cuadrado'),
    ('MA', 'Mayor a un metro cuadrado'),
)

TIPO_CHOICES = (
    ('P', 'Pick-up'),
    ('S', 'Sedan'),
    ('M', 'Motocicleta'),
)

USO_CHOICES = (
    ('C', 'Carga'),
    ('P', 'Particular'),
)

ASIGNACION_CHOICES = (
    ('M', 'En Mantenimiento'),
    ('P', 'En Pauta'),
    ('D', 'Disponible'),
    ('C', 'En Comodato'),
    ('A', 'Asignado a Presidencia'),
)

ASIG_CHOFER_CHOICES = (
    ('V', 'De Vacaciones'),
    ('P', 'Dias Pendientes'),
    ('R', 'De Reposo'),
    ('D', 'Disponible'),
)

GRADOS_LICENCIA_CHOICES = (
    ('3', 'Licencia de 3er Grado'),
    ('4', 'Licencia de 4to Grado'),
    ('5', 'Licencia de 5to Grado'),
)

ENTRADA_SALIDA_CHOICES = (
    ('E', 'Entrada'),
    ('S', 'Salida'),
)

NIVEL_CHOICES = (
    ('1', 'Tanque lleno'),
    ('3/4', 'Tres cuartos de tanque'),
    ('1/2', 'Medio tanque'),
    ('0', 'Tanque vacío'),
)

ESTADO_CHOICES = (
    ('N', 'Nueva'),
    ('P', 'Por ejecutar'),
    ('E', 'Ejecutándose'),
    ('A', 'Anulada'),
    ('F', 'Finalizada'),
)

class Solicitud(models.Model):
    empleado = models.ForeignKey(Empleado)
    actividad_a_realizar = models.CharField(
        'Actividad a realizar', max_length=50)
    destino = models.CharField('Destino', max_length=50)
    salida = models.DateTimeField('Fecha y hora de salida', blank=True)
    llegada_aprox = models.DateTimeField(
        'Fecha y hora de llegada aproximada', blank=True)
    n_ocupantes = models.IntegerField('Numero de ocupantes del vehiculo')
    carretera = models.CharField(
        max_length=12, choices=CARRETERA_CHOICES, default='P')
    carga = models.CharField(
        max_length=40, choices=CARGA_CHOICES, default='NO')
    observaciones = models.TextField('Observaciones de la solicitud')
    estado_solicitud = models.CharField('Estado de la solicitud', choices=ESTADO_CHOICES, default='N', max_length=20)
    fecha_reg = models.DateTimeField()
    fecha_act = models.DateTimeField()

    class Meta:
        ordering = ["fecha_reg"]
        verbose_name_plural = "Solicitudes"

    def __str__(self):
        return u'%s' % (self.empleado)


class Vehiculo(models.Model):
    placa = models.CharField('Placa', max_length=10, unique=True)
    modelo = models.CharField('Modelo del Vehículo', max_length=10)
    color = models.CharField('Color del Vehículo', max_length=20)
    tipo = models.CharField(max_length=10, choices=TIPO_CHOICES, default='S')
    uso = models.CharField(max_length=11, choices=USO_CHOICES, default='P')
    n_puestos = models.IntegerField('Numero de puestos del vehiculo')
    capa_tanque_gasolina = models.IntegerField('Cantidad en litros')

    def __str__(self):
        return u'%s %s' % (self.placa, self.modelo)


class Chofer(models.Model):
    empleado = models.OneToOneField(Empleado)
    licencia_moto = models.BooleanField(default=False)
    licencia = models.CharField(
        'Grados de Licencia de Conducir', max_length=20, choices=GRADOS_LICENCIA_CHOICES)
    venc_licencia = models.DateField(
        'Fecha de vencimiento de la licencia de conducir')
    activo = models.BooleanField(default=False)
    tipo_asignacion_chofer = models.CharField(
        max_length=20, choices=ASIG_CHOFER_CHOICES, default='D')

    class Meta:
        ordering = ["empleado"]
        verbose_name_plural = "Choferes"

    def __str__(self):
        return u'%s' % (self.empleado)


class Asignacion(models.Model):
    vehiculo = models.ForeignKey(Vehiculo)
    chofer = models.ForeignKey(Chofer)
    fecha_reg = models.DateTimeField(auto_now_add=True)
    fecha_act = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["fecha_reg"]
        verbose_name_plural = "Asignaciones"

    def __str__(self):
        return u'%s %s' % (self.vehiculo, self.chofer)


class Bitacora(models.Model):
    asignacion = models.ForeignKey(Asignacion)
    fecha_hora = models.DateTimeField('Hora de llegada')
    nivel_tanque_gasolina = models.CharField(
        'Nivel del tanque de la gasolina', choices=NIVEL_CHOICES, max_length=10)
    kilometraje = models.FloatField(
        'Kilometraje', help_text='Cantidad en kilometros', max_length=10)
    observaciones = models.TextField('Observaciones del viaje')
    entrada_salida = models.CharField(
        max_length=20, choices=ENTRADA_SALIDA_CHOICES)
    fecha_reg = models.DateTimeField(auto_now_add=True)
    fecha_act = models.DateTimeField(auto_now=True)

    def __str__(self):
        return u'%s' % (self.asignacion)
