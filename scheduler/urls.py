from django.urls import path
from scheduler.views import schedule_view, roster_view, add_roster, edit_roster, delete_roster, view_calendar


urlpatterns = [
    path("", schedule_view, name="scheduler"),
    path("roster/", roster_view, name="roster"),
    path("roster/add/", add_roster, name="add_roster"),
    path("roster/edit/<int:id>/", edit_roster, name="edit_roster"),
    path("roster/delete/<int:id>/", delete_roster, name="delete_roster"),
    path("roster/calendar/", view_calendar, name="calendar"),
]
