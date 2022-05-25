from django.shortcuts import render
from django.http import HttpResponse

from .models import *
# Create your views here.

def index(request):
    item = Item.objects.all()
    return render(request, "auctions/index.html", {
        "items": item,
    })