from django.contrib import admin
from .models import Galeria
 
# Models.

class GaleriaAdmin(admin.ModelAdmin):
    readonly_fields=('created', 'updated')

admin.site.register(Galeria, GaleriaAdmin)