import pytest
import test_helpers

from django.urls import reverse
from django.test import Client


pytestmark = [pytest.mark.django_db]


def tests_Profile_list_view():
    instance1 = test_helpers.create_staff_app_Profile()
    instance2 = test_helpers.create_staff_app_Profile()
    client = Client()
    url = reverse("staff_app_Profile_list")
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance1) in response.content.decode("utf-8")
    assert str(instance2) in response.content.decode("utf-8")


def tests_Profile_create_view():
    client = Client()
    url = reverse("staff_app_Profile_create")
    data = {
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_Profile_detail_view():
    client = Client()
    instance = test_helpers.create_staff_app_Profile()
    url = reverse("staff_app_Profile_detail", args=[instance.pk, ])
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance) in response.content.decode("utf-8")


def tests_Profile_update_view():
    client = Client()
    instance = test_helpers.create_staff_app_Profile()
    url = reverse("staff_app_Profile_update", args=[instance.pk, ])
    data = {
    }
    response = client.post(url, data)
    assert response.status_code == 302
