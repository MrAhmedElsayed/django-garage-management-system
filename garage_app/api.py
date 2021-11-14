from rest_framework import viewsets, permissions

from . import serializers
from . import models


class TicketViewSet(viewsets.ModelViewSet):
    """ViewSet for the Ticket class"""

    queryset = models.Ticket.objects.all()
    serializer_class = serializers.TicketSerializer
    permission_classes = [permissions.IsAuthenticated]
