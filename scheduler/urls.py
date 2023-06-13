from django.urls import path
from scheduler.views import schedule_view, roster_view, add_roster, edit_roster


urlpatterns = [
    path("", schedule_view, name="scheduler"),
    path("roster/", roster_view, name="roster"),
    path("roster/add/", add_roster, name="add_roster"),
    path("roster/edit/<int:id>/", edit_roster, name="edit_roster"),
]
