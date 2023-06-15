from django.db import models
from django.conf import settings
# Create your models here.

class WowClass(models.Model):
    character_class = models.CharField(max_length=20)

    def __str__(self):
        return self.character_class

class WowRole(models.Model):
    role = models.CharField(max_length=40)

    def __str__(self):
        return self.role

class WowSecondaryRole(models.Model):
    secondary_role = models.CharField(max_length=40, null=True)

    def __str__(self):
        return self.secondary_role

class WowTeam(models.Model):
    team = models.CharField(max_length=35, null=True)

    def __str__(self):
        return self.team

class Character(models.Model):
    name = models.CharField(max_length=35)
    primary_role = models.ForeignKey(
        WowRole,
        related_name="character",
        on_delete=models.CASCADE,
        )
    secondary_role = models.ForeignKey(
        WowSecondaryRole,
        related_name="character",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    character_class = models.ForeignKey(
        WowClass,
        related_name="character",
        on_delete=models.CASCADE,
    )
    owner  = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name="character",
        on_delete=models.CASCADE,
    )
    team = models.ForeignKey(
        WowTeam,
        related_name="character",
        on_delete=models.CASCADE,
        null=True,
    )
    def __str__(self):
        return self.name


class Event(models.Model):
    name = models.CharField(max_length=100)
    participants = models.ManyToManyField(Character)
