from django.shortcuts import render
from properties.models import Property
from realtors.models import Realtor
from .models import About


def about(request):
    realtors = Realtor.objects.order_by('-hire_date')
    abouts = About.objects.all()
    context = {
        'realtors': realtors,
        'abouts': abouts
    }
    return render(request, 'about/about.html', context)
