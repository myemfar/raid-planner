# Generated by Django 4.2.2 on 2023-06-13 17:32

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        (
            "scheduler",
            "0004_wowsecondaryrole_rename_role_character_primary_role_and_more",
        ),
    ]

    operations = [
        migrations.AlterField(
            model_name="wowsecondaryrole",
            name="secondary_role",
            field=models.CharField(max_length=40, null=True),
        ),
    ]
