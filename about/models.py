from django.db import models


class About(models.Model):
    name = models.CharField(max_length=200)
    heading_1 = models.CharField(max_length=400)
    heading_2 = models.CharField(max_length=400)
    about_description = models.TextField(blank=True)
    about_image = models.ImageField(upload_to='photos/%yy/%m/%d/')

    def __str__(self):
        return self.name


class Work(models.Model):
    heading = models.CharField(max_length=200)
    description = models.CharField(max_length=200)

    def __str__(self):
        return self.heading


class OurTeam(models.Model):
    team_name = models.CharField(max_length=100)
    team_image = models.ImageField(upload_to='photos/%Y/%m/%d/')
    phone_number = models.CharField(max_length=11)

    def __str__(self):
        return self.team_name
