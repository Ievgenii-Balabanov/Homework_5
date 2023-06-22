from math import sqrt

from django.shortcuts import render

from .forms import Triangle


def index(request):
    return render(request, "catalog/index.html")


gip = None


def get_cathetus(request):
    if request.POST:
        form = Triangle(request.POST)
        if form.is_valid():
            first_leg = form.cleaned_data["first_leg"]
            second_leg = form.cleaned_data["second_leg"]
            global gip
            gip = sqrt(first_leg**2 + second_leg**2)
            return render(request, "catalog/forms.html", {"form": form, "gip": gip})
    else:
        form = Triangle()

    return render(request, "catalog/forms.html", {"form": form})
