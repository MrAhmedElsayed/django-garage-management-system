from django.urls import path, include
from rest_framework import routers

from . import api
from . import views


router = routers.DefaultRouter()
router.register("Ticket", api.TicketViewSet)

urlpatterns = (
    path("api/v1/", include(router.urls)),
    path("garage_app/Ticket/", views.TicketListView.as_view(), name="garage_app_Ticket_list"),
    path("garage_app/Ticket/create/", views.TicketCreateView.as_view(), name="garage_app_Ticket_create"),
    path("garage_app/Ticket/detail/<int:pk>/", views.TicketDetailView.as_view(), name="garage_app_Ticket_detail"),
    path("garage_app/Ticket/update/<int:pk>/", views.TicketUpdateView.as_view(), name="garage_app_Ticket_update"),
    path("garage_app/Ticket/delete/<int:pk>/", views.TicketDeleteView.as_view(), name="garage_app_Ticket_delete"),
)
