# Generated by Django 4.2.2 on 2023-06-13 16:48

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("scheduler", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="character",
            name="role",
        ),
        migrations.AddField(
            model_name="character",
            name="role",
            field=models.ManyToManyField(to="scheduler.wowrole"),
        ),
    ]
