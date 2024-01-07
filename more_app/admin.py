from django.contrib import admin

from .models import MeyoriyXujjatlar, OqituvchiKategoriyalari

class OqituvchiKategoriyalariAdmin(admin.ModelAdmin):
    list_display = ['nomi']
admin.site.register(OqituvchiKategoriyalari, OqituvchiKategoriyalariAdmin)

class MeyoriyXujjatlarAdmin(admin.ModelAdmin):
    list_display = ['nomi', 'fayl', 'kategoriyasi']
admin.site.register(MeyoriyXujjatlar, MeyoriyXujjatlarAdmin)
