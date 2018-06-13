from django.views.generic import FormView
from django.shortcuts import render
from django.core.mail import BadHeaderError, EmailMessage
from django.http import HttpResponse, HttpResponseRedirect
from homepage.forms import ContactForm


class HomePageView(FormView):
    template_name = 'home.html'
    form_class = ContactForm
    success_url = '/thanks/'

    def form_valid(self, form):
        contact_name = form.cleaned_data['contact_name']
        contact_email = form.cleaned_data['contact_email']
        message = form.cleaned_data['content']
        try:
            email = EmailMessage(contact_name,
                                 message,
                                 contact_email,
                                 ['sales@bridsystems.com'],
                                 reply_to=[contact_email],
                                 )
            email.send()
        except BadHeaderError:
            return HttpResponse('Invalid header found')
        return HttpResponseRedirect('/')


def java_download(request):
    return render(request, 'java_download.html')
