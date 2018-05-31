from django.urls import path
from .views import IndexView, ContactMessageCreateView

app_name = 'website'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('contact/', ContactMessageCreateView.as_view(), name='contact')
]
