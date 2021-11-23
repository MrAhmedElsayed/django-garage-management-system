from django.urls import path, include
from rest_framework import routers

from . import api
from .views import TicketDeleteView, TicketDetailView, TicketUpdateView, home, create_ticket_view, ticket_detail


# router = routers.DefaultRouter()
# router.register("Ticket", api.TicketViewSet)

urlpatterns = (
    # path("api/v1/", include(router.urls)),

    path("create_ticket_view/", create_ticket_view, name="create_ticket_view"),

    path("ticket_detail/<int:pk>", ticket_detail, name="ticket_detail"),

    path("", home, name="home"),

    path("garage_app/Ticket/create/", create_ticket_view, name="garage_app_Ticket_create"),

    path("garage_app/Ticket/detail/<int:pk>/", TicketDetailView.as_view(), name="garage_app_Ticket_detail"),
    path("garage_app/Ticket/update/<int:pk>/", TicketUpdateView.as_view(), name="garage_app_Ticket_update"),
    path("garage_app/Ticket/delete/<int:pk>/", TicketDeleteView.as_view(), name="garage_app_Ticket_delete"),
)
