from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.views import generic
from django.urls import reverse_lazy
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from .forms import TicketForm
from .serializers import TicketSerializer
from .models import Ticket
from . import forms
from django.views.decorators.csrf import csrf_exempt
from rest_framework.permissions import IsAuthenticated
"""
https://www.geeksforgeeks.org/function-based-views-django-rest-framework/"""


@login_required
def home(request):
    context = dict()
    context["tickets"] = Ticket.objects.all().order_by('created')
    return render(request, template_name='garage_app/index.html', context=context)


# def create_ticket_view(request):
#     form = TicketForm()
#     if request.method == 'POST':
#         form = TicketForm(request.POST)
#
#         if form.is_valid():
#             print('Valid form')
#             form_instance = TicketForm(request.POST).save(commit=False)
#             form_instance.employee = request.user
#             form_instance.ticket_total_price = float(form_instance.reservation_time_per_day) * float(
#                 form_instance.parking_price_per_day)
#             form_instance.save()
#             return redirect('/')
#
#     return render(request, template_name='garage_app/index.html', context={
#         'form': form
#     })


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_ticket_view(request):
    if request.method == 'POST':
        serializer = TicketSerializer(data=request.data['ticket_form_data'])
        print(request.data['ticket_form_data'])
        print(request.user)
        if serializer.is_valid():
            serializer.save(employee=request.user, ticket_total_price=12)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# @api_view(['GET', 'POST'])
# def snippet_list(request):
#     """
#     List all code snippets, or create a new snippet.
#     """
#     if request.method == 'GET':
#         snippets = Snippet.objects.all()
#         serializer = SnippetSerializer(snippets, many=True)
#         return Response(serializer.data)
#
#     elif request.method == 'POST':
#         serializer = SnippetSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TicketDetailView(generic.DetailView):
    model = Ticket
    form_class = forms.TicketForm


class TicketUpdateView(generic.UpdateView):
    model = Ticket
    form_class = forms.TicketForm
    pk_url_kwarg = "pk"


class TicketDeleteView(generic.DeleteView):
    model = Ticket
    success_url = reverse_lazy("garage_app_Ticket_list")
