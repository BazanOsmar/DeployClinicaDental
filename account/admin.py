from django.contrib import admin
from . import models
# Register your models here.

admin.site.register(models.Roles)
admin.site.register(models.ExtraInfo)
admin.site.register(models.Citas)
admin.site.register(models.Tratamiento)
admin.site.register(models.Horarios)
admin.site.register(models.TipoTratamiento)
admin.site.register(models.Estado)
