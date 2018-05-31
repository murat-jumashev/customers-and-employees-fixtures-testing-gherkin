from django.urls import reverse
from django.http import JsonResponse
from django.shortcuts import render
from django.contrib import messages
from django.views.generic import TemplateView, CreateView

from .models import ContactMessage


class AjaxableResponseMixin:
    """
    Mixin to add AJAX support to a form.
    Must be used with an object-based FormView (e.g. CreateView)
    """
    def form_invalid(self, form):
        response = super().form_invalid(form)
        if self.request.is_ajax():
            return JsonResponse(form.errors, status=400)
        else:
            return response

    def form_valid(self, form):
        # We make sure to call the parent's form_valid() method because
        # it might do some processing (in the case of CreateView, it will
        # call form.save() for example).
        response = super().form_valid(form)
        if self.request.is_ajax():
            data = {
                'pk': self.object.pk,
                'name': self.object.name,
                'email': self.object.email,
                'text': self.object.text,
                'datetime_created': self.object.datetime_created
            }
            return JsonResponse(data)
        else:
            return response


class IndexView(TemplateView):
    template_name = 'website/index.html'


class ContactMessageCreateView(AjaxableResponseMixin, CreateView):
    model = ContactMessage
    template_name = 'website/contact_message.html'
    fields = '__all__'

    def get_success_url(self):
        # message = 'Ваше сообщение успешно отправлено. Спасибо!'
        # messages.add_message(self.request, messages.SUCCESS, message)
        return reverse('website:contact')
