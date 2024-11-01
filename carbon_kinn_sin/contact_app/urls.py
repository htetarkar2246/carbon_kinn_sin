from django.urls import path
from .views import ContactMessageView

urlpatterns = [
    path('contact-us/', ContactMessageView.as_view(), name='contact_message'),
]