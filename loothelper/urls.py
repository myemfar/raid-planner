from django.urls import path
from loothelper.views import loot_helper

urlpatterns = [
    path("loothelper/", loot_helper, name="loot_helper"),
]
