from django.contrib import admin
from Familia.models import Familiares, Sobre_mi

# Register your models here.

class FamiliaresAdmin(admin.ModelAdmin):
    list_display= ("nombre","edad","parentesco","f_nacimiento")
class Sobre_miAdmin(admin.ModelAdmin):
    list_display= ("nombre","edad","telefono")

admin.site.register(Familiares,FamiliaresAdmin)
admin.site.register(Sobre_mi,Sobre_miAdmin)