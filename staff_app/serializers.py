from rest_framework import serializers

from . import models


class ProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Profile
        fields = [
            "last_updated",
            "created",
        ]
