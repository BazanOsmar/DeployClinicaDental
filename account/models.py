from django.db import models
from django.contrib.auth.models import User

class Roles(models.Model):
    rol = models.CharField(max_length=100)

    def __str__(self):
        return self.rol

class ExtraInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    numero_celular = models.CharField(max_length=15, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    rol = models.ForeignKey(Roles, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user.username} Profile'

class Horarios(models.Model):
    hora_inicio = models.TimeField()
    hora_fin = models.TimeField()
    fecha = models.DateField()

    def __str__(self):
        return f'{self.fecha} {self.hora_inicio} - {self.hora_fin}'

class Estado(models.Model):
    descripcion_estado = models.CharField(max_length=200)

    def __str__(self):
        return self.descripcion_estado

class TipoTratamiento(models.Model):
    nombre_tratamiento = models.CharField(max_length=150)

    def __str__(self):
        return self.nombre_tratamiento

class Tratamiento(models.Model):
    precio = models.FloatField()
    estado = models.ForeignKey(Estado, on_delete=models.CASCADE)
    descripcion_tratamiento = models.TextField()
    paciente = models.ForeignKey(User, on_delete=models.CASCADE)    
    tipo_tratamiento = models.ForeignKey(TipoTratamiento, on_delete=models.CASCADE)

    """def __str__(self):
        return f'{self.descripcion_tratamiento} ({self.precio})'"""

class Citas(models.Model):
    paciente = models.ForeignKey(User, on_delete=models.CASCADE)
    tratamiento = models.ForeignKey(Tratamiento, on_delete=models.CASCADE)
    horario = models.ForeignKey(Horarios, on_delete=models.CASCADE)
    estado = models.ForeignKey(Estado, on_delete=models.CASCADE)
    pago_completado = models.BooleanField(default=False)

    """def __str__(self):
        return f'Cita {self.paciente.username} - {self.tratamiento}'"""

class Pagos(models.Model):
    fecha = models.DateField()
    monto = models.FloatField()
    paciente = models.ForeignKey(User, on_delete=models.CASCADE)
    tratamiento = models.ForeignKey(Tratamiento, on_delete=models.CASCADE)
    cita = models.ForeignKey(Citas, on_delete=models.CASCADE)

    def __str__(self):
        return f'Pago {self.monto} - {self.fecha}'
