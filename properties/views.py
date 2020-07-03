# noinspection PyUnresolvedReferences
from django.shortcuts import render, get_object_or_404
from .models import *
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from properties.choices import *


def properties(request):
    propertys = Property.objects.order_by('-property_date').filter(is_published=True)
    paginator = Paginator(propertys, 3)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)
    context = {
        'listings': paged_listings
    }
    return render(request, 'properties/properties.html', context)


def property(request, property_id):
    listing = get_object_or_404(Property, pk=property_id)
    context = {
        'listing': listing
    }
    return render(request, 'properties/property.html', context)


def search(request):
    queryset_list = Property.objects.order_by('-property_date')
    # sale_or_rent
    if 'sale_or_rent' in request.GET:
        sale_or_rent = request.GET['sale_or_rent']
        if sale_or_rent:
            queryset_list = queryset_list.filter(sale_or_rent__iexact=sale_or_rent)
    if 'lot_size' in request.GET:
        lot_size = request.GET['lot_size']
        if lot_size:
            queryset_list = queryset_list.filter(title__icontains=lot_size)
    context = {
        'rent_sale_choices': rent_sale_choices,
        'lot_size_choices': lot_size_choices,
        'residential_choices': residential_choices,
        'commercial_choices': commercial_choices,
        'listings': queryset_list,
        'values': request.GET,
    }
    return render(request, 'properties/search.html', context)
