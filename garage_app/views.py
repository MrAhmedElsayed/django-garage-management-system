from django.views import generic
from django.urls import reverse_lazy
from . import models
from . import forms



class TicketListView(generic.ListView):
    model = models.Ticket
    form_class = forms.TicketForm


class TicketCreateView(generic.CreateView):
    template_name = 'index.html'
    model = models.Ticket
    form_class = forms.TicketForm


class TicketDetailView(generic.DetailView):
    model = models.Ticket
    form_class = forms.TicketForm


class TicketUpdateView(generic.UpdateView):
    model = models.Ticket
    form_class = forms.TicketForm
    pk_url_kwarg = "pk"


class TicketDeleteView(generic.DeleteView):
    model = models.Ticket
    success_url = reverse_lazy("garage_app_Ticket_list")
