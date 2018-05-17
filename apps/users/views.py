from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.views.generic.edit import FormMixin

from .forms import UserForm, choices
from .models import User, Customer, Employee


EMPLOYEE = choices[0][0]
CUSTOMER = choices[1][0]


class RegistrationView(FormMixin, TemplateView):
    template_name = 'registration/user_registration.html'
    form_class = UserForm
    success_url = reverse_lazy('website:index')

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            type_of_user = form.cleaned_data['type_of_user']
            profile_class = Employee
            if type_of_user == CUSTOMER:
                profile_class = Customer
            user = form.save()
            profile_class.objects.create(user=user)              #pylint: disable=E1101,another-one
        return redirect(self.success_url)

