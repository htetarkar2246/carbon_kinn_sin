from django.urls import path
from .views import ContactMessageView, ReportCreateView

urlpatterns = [
    path('contact-us/', ContactMessageView.as_view(), name='contact_message'),
    path('reports/', ReportCreateView.as_view(), name='report-create'),
]