from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from scheduler.models import Character, Event
from scheduler.forms import AddCharacterForm
# Create your views here.

def roster_view(request):
    roster = Character.objects.all()
    context = {
        "roster": roster,
    }
    return render(request, "scheduler/roster.html", context)

def schedule_view(request):
    return redirect("home")


def add_roster(request):
    if request.method == "POST":
        form = AddCharacterForm(request.POST)
        if form.is_valid():
            character = form.save(False)
            character.owner = request.user
            character.save()
            return redirect("home")
    else:
        form = AddCharacterForm()
    context = {
        "form": form,
    }
    return render(request, "scheduler/create.html", context)


def edit_roster(request, id):
    post = get_object_or_404(Character, id=id)
    if request.method == "POST":
        form = AddCharacterForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = AddCharacterForm(instance=post)
    context = {
        "form": form,
        "object": post,
    }
    return render(request, "scheduler/edit.html", context)

def delete_roster(request, id):
    post = get_object_or_404(Character, id=id)
    context = {
        "post": post
    }
    if request.method == "GET":
        return render(request, "scheduler/delete.html", context)
    elif request.method == "POST":
        post.delete()
        messages.success(request, "The character has been deleted successfully.")
        return redirect("home")

def view_calendar(request):
    calendar = Event.objects.all()
    context = {
        "calendar": calendar
    }
    return render(request, "scheduler/calendar.html", context)
