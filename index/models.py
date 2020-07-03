from django.db import models


class Service(models.Model):
    consulting_service = models.CharField(max_length=200)
    consulting_description = models.TextField(blank=True)
    property_management = models.CharField(max_length=200)
    property_description = models.TextField(blank=True)
    renting_selling = models.CharField(max_length=200)
    r_s_description = models.TextField(blank=True)

    def __str__(self):
        return self.consulting_service
