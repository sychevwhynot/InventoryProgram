from django.contrib import admin
from .models import Sklads, Etazh, Kabinet, Edinica

class EtazhInline(admin.TabularInline):
    model = Etazh

class KabinetInline(admin.TabularInline):
    model = Kabinet

class EdinicaInline(admin.TabularInline):
    model = Edinica

class SkladAdmin(admin.ModelAdmin):
    inlines = [EtazhInline]

admin.site.register(Sklads, SkladAdmin)

class EtazhAdmin(admin.ModelAdmin):
    inlines = [KabinetInline]
    list_display = ('title', 'sklad')

admin.site.register(Etazh, EtazhAdmin)

class KabinetAdmin(admin.ModelAdmin):
    inlines = [EdinicaInline]
    list_display = ('title', 'get_sklad', 'get_etazh')  
    
    def get_sklad(self, obj):
        return obj.etazh.sklad if obj.etazh else None
    
    get_sklad.short_description = 'Склад'  # Задаем краткое описание поля

    def get_etazh(self, obj):
        return obj.etazh
    
    get_etazh.short_description = 'Этаж'

admin.site.register(Kabinet, KabinetAdmin)

class EdinicaAdmin(admin.ModelAdmin):
    list_display = ('title', 'seriniy', 'invent', 'sklad', 'etazh', 'kabinet', 'brand', 'model', 'remont', 'lico', 'mac')

admin.site.register(Edinica, EdinicaAdmin)
