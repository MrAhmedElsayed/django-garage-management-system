from django.urls import path

from garage_app.api import ticket_list, ticket_detail
from garage_app.views import home

urlpatterns = (
    path("", home, name="home"),
    path("ticket_list/", ticket_list, name="ticket_list"),
    path("ticket_detail/<int:pk>", ticket_detail, name="ticket_detail"),
)
