from django.urls import path
from scheduler.views import schedule_view


urlpatterns = [
    path("scheduler/", schedule_view, name="scheduler"),
]
