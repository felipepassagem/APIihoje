from django.contrib import admin

# Register your models here.
from .models import Venue

@admin.register(Venue)
class VenueAdmin(admin.ModelAdmin):
    list_display = ('name', 'owner', 'city')  # Campos a serem exibidos na lista de estabelecimentos
    list_filter = ('owner', 'city')  # Filtros disponíveis na administração
    search_fields = ('name', 'city')  # Campo de pesquisa

    # Outras configurações de administração, como fieldsets, list_editable, etc.
