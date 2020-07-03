# noinspection PyUnresolvedReferences
from django.urls import path
from .import views

urlpatterns = [
    path('/properties', views.properties, name='properties'),
    path('/<int:property_id>', views.property, name='property'),
    path('search', views.search, name='search'),
]