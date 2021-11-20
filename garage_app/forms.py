from django import forms
from . import models


class TicketForm(forms.ModelForm):
    class Meta:
        model = models.Ticket
        fields = [
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
            "employee"
        ]
        exclude = ("employee", "completed", "ticket_total_price",)   #
