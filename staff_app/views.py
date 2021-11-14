from django.views import generic
from django.urls import reverse_lazy
from . import models
from . import forms


class ProfileListView(generic.ListView):
    model = models.Profile
    form_class = forms.ProfileForm


class ProfileCreateView(generic.CreateView):
    model = models.Profile
    form_class = forms.ProfileForm


class ProfileDetailView(generic.DetailView):
    model = models.Profile
    form_class = forms.ProfileForm


class ProfileUpdateView(generic.UpdateView):
    model = models.Profile
    form_class = forms.ProfileForm
    pk_url_kwarg = "pk"


class ProfileDeleteView(generic.DeleteView):
    model = models.Profile
    success_url = reverse_lazy("staff_app_Profile_list")
