from django.contrib import admin
from django import forms

from . import models


class ProfileAdminForm(forms.ModelForm):

    class Meta:
        model = models.Profile
        fields = "__all__"


class ProfileAdmin(admin.ModelAdmin):
    form = ProfileAdminForm
    list_display = [
        "last_updated",
        "created",
    ]
    readonly_fields = [
        "last_updated",
        "created",
    ]


admin.site.register(models.Profile, ProfileAdmin)
