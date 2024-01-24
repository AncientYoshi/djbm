from django.shortcuts import render
from app_p3.forms import InputForm
from django.http import HttpResponse

# Create your views here.


def form_view(request):
    form = InputForm()
    context = {"form": form}
    return render(request, "home.html", context)
