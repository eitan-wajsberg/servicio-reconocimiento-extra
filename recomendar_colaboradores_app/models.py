from django.db import models
from datetime import date

class Colaborador(models.Model):
    tipo_documento = models.CharField(max_length=10)
    nro_documento = models.CharField(max_length=8)
    direccion = models.CharField(max_length=255)
    nombre = models.CharField(max_length=250)
    apellido = models.CharField(max_length=255)
    fecha_nacimiento = models.DateField()
    whatsapp = models.CharField(max_length=255, blank=True, null=True)
    mail = models.EmailField(max_length=255, blank=True, null=True)
    user_telegram = models.CharField(max_length=255, blank=True, null=True)
    puntaje_neto = models.DecimalField(max_digits=10, decimal_places=2)
    cantidad_viandas_ultimo_mes = models.IntegerField()
    
    class Meta:
        db_table = 'colaborador_reconocido'

class Solicitante(models.Model):
    razon_social = models.CharField(max_length=255)
    rubro = models.CharField(max_length=255)
    whatsapp = models.CharField(max_length=255, blank=True, null=True)
    mail = models.EmailField(max_length=255, blank=True, null=True)
    user_telegram = models.CharField(max_length=255, blank=True, null=True)
    direccion = models.CharField(max_length=255)

    class Meta:
        db_table = 'solicitante'

class Solicitud(models.Model):
    cant_min_puntos = models.IntegerField()
    cant_min_viandas_ultimo_mes = models.IntegerField()
    fecha = models.DateField()
    cant_max_colaboradores = models.IntegerField()
    solicitante = models.ForeignKey(Solicitante, on_delete=models.CASCADE)

    class Meta:
        db_table = 'solicitud'

class Recomendacion(models.Model):
    solicitud = models.ForeignKey(Solicitud, on_delete=models.CASCADE)
    colaboradores = models.ManyToManyField('Colaborador')
    fecha_recomendacion = models.DateField(default=date.today)

    class Meta:
        db_table = 'recomendacion'

