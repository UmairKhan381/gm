from django.shortcuts import render, redirect
from .models import Contact
from django.contrib import messages
from django.core.mail import send_mail


def contact(request):
    if request.method == 'POST':
        property_id = request.POST['property_id']
        property = request.POST['property']
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        realtor_email = request.POST['realtor_email']
        user_id = request.POST['user_id']

        #  Check if user has made inquiry already
        if request.user.is_authenticated:
            user_id = request.user.id
            has_contacted = Contact.objects.all().filter(property_id=property_id, user_id=user_id)
            if has_contacted:
                messages.error(request, 'You have already made inquiry for this property')
                return redirect('/properties/'+property_id)

        contact = Contact(property=property, property_id=property_id, phone=phone,
                          name=name, email=email, message=message, user_id=user_id)
        contact.save()
        # send email
        send_mail(
            'PROPERTY LISTING INQUIRY',
            'THERE HAS BEEN AN INQUIRY FOR ' + property + '. SIGN INTO THE ADMIN PANEL',
            'uk938216@gmail.com',
            [realtor_email, email],
            fail_silently=False
        )

        messages.success(request, 'Your request has been submitted, a realtor will get back to you soon')

        return redirect('/properties/'+property_id)
