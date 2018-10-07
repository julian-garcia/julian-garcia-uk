from django.shortcuts import render
from django.core.mail import send_mail
from .forms import ContactForm
import os

def contact(request):
    contact_form = ContactForm()

    if request.method == 'POST':
        send_mail('Message: julian-garcia.uk',
                  request.POST.get('message'),
                  request.POST.get('email_address'),
                  [os.environ.get('EMAIL_HOST_USER')],
                  fail_silently=False)
        post_message = 'Thank you - your message has been delivered'
        return render(request, 'contact.html', {'contact_form': contact_form,
                                                'post_message': post_message})
    else:
        return render(request, 'contact.html', {'contact_form': contact_form})
