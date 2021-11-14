from django.urls import path, include
from rest_framework import routers

from . import api
from . import views


router = routers.DefaultRouter()
router.register("Profile", api.ProfileViewSet)

urlpatterns = (
    path("api/v1/", include(router.urls)),
    path("staff_app/Profile/", views.ProfileListView.as_view(), name="staff_app_Profile_list"),
    path("staff_app/Profile/create/", views.ProfileCreateView.as_view(), name="staff_app_Profile_create"),
    path("staff_app/Profile/detail/<int:pk>/", views.ProfileDetailView.as_view(), name="staff_app_Profile_detail"),
    path("staff_app/Profile/update/<int:pk>/", views.ProfileUpdateView.as_view(), name="staff_app_Profile_update"),
    path("staff_app/Profile/delete/<int:pk>/", views.ProfileDeleteView.as_view(), name="staff_app_Profile_delete"),
)
