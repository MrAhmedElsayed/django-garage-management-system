import pytest
import test_helpers

from django.urls import reverse
from django.test import Client


pytestmark = [pytest.mark.django_db]


def tests_Ticket_list_view():
    instance1 = test_helpers.create_garage_app_Ticket()
    instance2 = test_helpers.create_garage_app_Ticket()
    client = Client()
    url = reverse("garage_app_Ticket_list")
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance1) in response.content.decode("utf-8")
    assert str(instance2) in response.content.decode("utf-8")


def tests_Ticket_create_view():
    client = Client()
    url = reverse("garage_app_Ticket_create")
    data = {
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_Ticket_detail_view():
    client = Client()
    instance = test_helpers.create_garage_app_Ticket()
    url = reverse("garage_app_Ticket_detail", args=[instance.pk, ])
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance) in response.content.decode("utf-8")


def tests_Ticket_update_view():
    client = Client()
    instance = test_helpers.create_garage_app_Ticket()
    url = reverse("garage_app_Ticket_update", args=[instance.pk, ])
    data = {
    }
    response = client.post(url, data)
    assert response.status_code == 302
