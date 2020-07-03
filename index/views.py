from django.shortcuts import render
from django.http import HttpResponse
from properties.models import *
from properties.choices import *
# Create your views here.


def index(request):
    listings = Property.objects.order_by('-property_date').filter(is_published=True)[:3]
    context = {
        'listings': listings,
        'rent_sale_choices': rent_sale_choices,
        'lot_size_choices': lot_size_choices,
        'residential_choices': residential_choices,
        'commercial_choices': commercial_choices,
    }
    return render(request, 'index/index.html', context)
