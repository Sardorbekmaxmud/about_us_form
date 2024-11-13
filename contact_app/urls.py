from django.urls import path
from .views import contact_form, contact_list

urlpatterns = [
    path('', contact_form, name='contact-form'),
    path('list/', contact_list, name='customer-list'),
]
