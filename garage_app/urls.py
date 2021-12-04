from django.urls import path

from garage_app.api import ticket_list, ticket_detail
from garage_app.views import home, ticket_management, qr_generator
from garage_app.utils import PrintView

urlpatterns = (
    path("", home, name="home"),
    path("ticket/management/", ticket_management, name="ticket_management"),
    path("ticket_list/", ticket_list, name="ticket_list"),
    path("ticket_detail/<int:pk>", ticket_detail, name="ticket_detail"),

    # pdf
    path("pdf/<int:pk>/", PrintView.as_view(), name="pdf_print"),

    path("qr_generator/", qr_generator, name="qr_generator"),
)
