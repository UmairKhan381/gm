from django.contrib import admin
from .models import Contact


class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'property', 'email', 'contact_date')
    list_display_links = ('id', 'name')
    search_field = ('name', 'email', 'property')
    list_per_page = 25


admin.site.register(Contact, ContactAdmin)
