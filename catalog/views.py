from math import sqrt

from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.views import generic

from .forms import PersonModelForm, Triangle
from .models import Person


# --------------------------------------------------------
# --> Triangle view
# gip = None


# def get_cathetus(request):
#     if request.POST:
#         form = Triangle(request.POST)
#         if form.is_valid():
#             first_leg = form.cleaned_data["first_leg"]
#             second_leg = form.cleaned_data["second_leg"]
#             global gip
#             gip = sqrt(first_leg**2 + second_leg**2)
#             return render(request, "catalog/forms.html", {"form": form, "gip": gip})
#     else:
#         form = Triangle()
#
#     return render(request, "catalog/forms.html", {"form": form})
# ------------------------------------------------------------------


class IndexView(generic.ListView):
    template_name = "catalog/index.html"
    queryset = Person.objects.all()


class PersonDetailView(generic.DetailView):
    model = Person
    template_name = "catalog/detail.html"


def create_person(request):
    if request.POST:
        form = PersonModelForm(request.POST)
        if form.is_valid():
            person = form.save()
            return redirect(reverse("catalog:detail", args=(person.id,)))
    else:
        form = PersonModelForm()
    return render(request, "catalog/create_person.html", {"form_create": form})


def update_person(request, pk):
    person = get_object_or_404(Person, pk=pk)
    if request.POST:
        form = PersonModelForm(request.POST, instance=person)
        if form.is_valid():
            form.save()
            return redirect(reverse("catalog:detail", args=(person.id,)))
    else:
        form = PersonModelForm(instance=person)
    return render(request, "catalog/create_person.html", {"form_create": form, "person": person})


def delete_person(request, pk):
    person = get_object_or_404(Person, pk=pk)
    if request.POST:
        person.delete()
        return redirect(reverse("catalog:index"))
    else:
        form = PersonModelForm()
    return render(request, "catalog/delete_person.html", {"form_delete": form, "person": person})
