from django.forms import ModelForm
from scheduler.models import Character


class AddCharacterForm(ModelForm):
    class Meta:
        model = Character
        fields = [
            "name",
            "primary_role",
            "secondary_role",
            "character_class",
        ]
