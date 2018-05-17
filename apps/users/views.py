from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import TemplateView
from django.views.generic.edit import FormMixin
from django.core.mail import EmailMessage
from django.contrib.auth import login
from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode

from .forms import UserForm, choices
from .models import User, Customer, Employee
from .tokens import account_activation_token


EMPLOYEE = choices[0][0]
CUSTOMER = choices[1][0]


class RegistrationView(FormMixin, TemplateView):
    template_name = 'registration/user_registration.html'
    email_template = 'registration/activation_email.html'
    form_class = UserForm
    success_url = reverse_lazy('website:index')

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            type_of_user = form.cleaned_data['type_of_user']
            user = form.save(commit=False)
            user.is_active = False
            user.save()

            current_site = get_current_site(request)
            mail_subject = 'Activate your account.'
            message = render_to_string(self.email_template, {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)).decode(),
                'token': account_activation_token.make_token(user),
                'type_of_user': type_of_user
            })
            to_email = form.cleaned_data.get('email')
            email = EmailMessage(mail_subject, message, to=[to_email])
            email.send()

            confirm_message = 'Email дарегиңизди тастыктаңыз'
            return render(request, self.template_name, {'message': confirm_message })
        return render(request, self.template_name, {'message': 'error', 'form': form })


class ActivationView(TemplateView):
    template_name = 'registration/activation_page.html'

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        uidb64 = kwargs.get('uidb64', None)
        token = kwargs.get('token', None)
        type_of_user = kwargs.get('type_of_user', None)
        try:
            uid = force_text(urlsafe_base64_decode(uidb64))
            user = User.objects.get(pk=uid)
        except(TypeError, ValueError, OverflowError, User.DoesNotExist):
            user = None
        if user is not None and account_activation_token.check_token(user, token):
            user.is_active = True
            user.save()
            profile_class = Employee
            if type_of_user == CUSTOMER:
                profile_class = Customer
            profile_class.objects.create(user=user)                                    #pylint: disable=E1101,another-one
            login(request, user)
            return redirect(reverse('website:index'))
        context['message'] = 'Activation url is wrong!'
        return self.render_to_response(context)
