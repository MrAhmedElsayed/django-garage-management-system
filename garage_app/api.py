from io import BytesIO

import qrcode
import qrcode.image.svg
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import Ticket
from .serializers import TicketSerializer


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def ticket_list(request):
    """
    HELP:
    # https://www.django-rest-framework.org/tutorial/2-requests-and-responses/
    # https://www.pluralsight.com/guides/work-with-ajax-django
    """
    # List all code snippets, or create a new snippet.
    if request.method == 'GET':
        snippets = Ticket.objects.all()
        serializer = TicketSerializer(snippets, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = TicketSerializer(data=request.data)

        factory = qrcode.image.svg.SvgImage
        img = qrcode.make(request.POST.get("qr_text", ""), image_factory=factory, box_size=20)
        stream = BytesIO()
        img.save(stream)
        svg = stream.getvalue().decode()

        if serializer.is_valid():
            # serializer.save()
            # serializer.save(employee=request.user, ticket_total_price=12, qr_code='')
            my_instance = serializer.save(employee=request.user, ticket_total_price=12, qr_code='')
            print(my_instance.id)

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@csrf_exempt
@api_view(['GET', 'PUT', 'DELETE'])
def ticket_detail(request, pk):
    """
    Retrieve, update or delete a ticket.
    """
    try:
        ticket = Ticket.objects.get(pk=pk)
    except Ticket.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = TicketSerializer(ticket)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = TicketSerializer(ticket, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        ticket.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
