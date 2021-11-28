from rest_framework import serializers

from . import models


class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Ticket
        fields = [
            "completed",
            "national_identification_number",
            "created",
            # "ticket_total_price",
            "parking_price_per_day",
            "car_color",
            "car_owner_name",
            "reservation_time_per_day",
            "owner_mobile_number",
            "car_model_name",
            "position_number",
            "last_updated",
            "car_model_year",
            "car_registration_no",
            "driver_license_number",
            "car_manufacturer",
            "car_chassis_no",
        ]
