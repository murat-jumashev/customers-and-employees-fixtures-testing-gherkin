from django.urls import path
from .views import (
    RegistrationView, ActivationView, CabinetView, ProfileEditView, CustomersList
)

app_name = 'users'

urlpatterns = [
    path('registration/', RegistrationView.as_view(), name='registration'),
    path(
        'activate/<str:uidb64>/<str:token>/<str:type_of_user>/',
        ActivationView.as_view(),
        name='activation'
    ),
    path('cabinet/', CabinetView.as_view(), name='cabinet'),
    path('cabinet/edit/', ProfileEditView.as_view(), name='edit'),
    path('customers-list/', CustomersList.as_view(), name='customers_list'),
]

