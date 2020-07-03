# Generated by Django 3.0.7 on 2020-06-21 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('heading_1', models.CharField(max_length=400)),
                ('heading_2', models.CharField(max_length=400)),
                ('about_description', models.TextField(blank=True)),
                ('about_image', models.ImageField(upload_to='photos/%yy/%m/%d/')),
            ],
        ),
        migrations.CreateModel(
            name='OurTeam',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('team_name', models.CharField(max_length=100)),
                ('team_image', models.ImageField(upload_to='photos/%Y/%m/%d/')),
                ('phone_number', models.CharField(max_length=11)),
            ],
        ),
        migrations.CreateModel(
            name='Work',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heading', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=200)),
            ],
        ),
    ]