from django.db import models
from django.urls import reverse


class Profile(models.Model):

    # Relationships
    employee = models.OneToOneField("auth.User", on_delete=models.CASCADE)

    # Fields
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    created = models.DateTimeField(auto_now_add=True, editable=False)

    class Meta:
        pass

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("staff_app_Profile_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("staff_app_Profile_update", args=(self.pk,))
