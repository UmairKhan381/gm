# noinspection PyUnresolvedReferences
from django.contrib import admin
from .models import Property


class PropertyAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'is_published', 'price', 'property_date', 'realtor')
    list_display_link = ('id', 'title')
    list_filter = ('realtor',)
    list_editable = ('is_published',)
    search_fields = ('title', 'description', 'location', 'price')
    list_per_page = 25


admin.site.register(Property, PropertyAdmin)

