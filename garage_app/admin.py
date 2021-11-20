from django.contrib import admin
from django import forms

from . import models


class TicketAdminForm(forms.ModelForm):
    class Meta:
        model = models.Ticket
        fields = "__all__"


class TicketAdmin(admin.ModelAdmin):
    form = TicketAdminForm
    list_display = [
        "car_owner_name",
        "owner_mobile_number",
        "national_identification_number",
        "driver_license_number",
        "car_model_year",
        "car_registration_no",
        "car_model_name",
        "car_manufacturer",
        "car_chassis_no",
        "car_color",
        "reservation_time_per_day",
        "ticket_total_price",
        "parking_price_per_day",
        "completed",
        "position_number",
    ]


admin.site.register(models.Ticket, TicketAdmin)
