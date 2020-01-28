from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.

from .models import *
import datetime
from .forms import *


def index(request):
    return render(request, 'index.html')

def display_Farhan(request):
    items = Farhan.objects.all()
    context = {
        'items': items,
        'header': 'Farhan',
    }
    return render(request, 'index.html', context)


def display_Nadia(request):
    items = Nadia.objects.all()
    context = {
        'items': items,
        'header': 'Nadia',
    }
    return render(request, 'index.html', context)


def display_FarhanFamilySuperFund(request):
    items = FarhanFamilySuperFund.objects.all()
    context = {
        'items': items,
        'header': 'Farhan Family Super Fund',
    }
    return render(request, 'index.html', context)

def display_Ongie(request):
    items = Ongie.objects.all()
    context = {
        'items': items,
        'header': 'Ongie',
    }
    return render(request, 'index.html', context)

def display_OrangeTrust(request):
    items = OrangeTrust.objects.all()
    context = {
        'items': items,
        'header': 'OrangeTrust',
    }
    return render(request, 'index.html', context)



def add_item(request, cls):
    if request.method == "POST":
        form = cls(request.POST)

        if form.is_valid():
            form.save()
            return redirect('index')

    else:
        form = cls()
        return render(request, 'add_new.html', {'form' : form})


def add_Farhan(request):
    return add_item(request, FarhanForm)


def add_Nadia(request):
    return add_item(request, NadiaForm)


def add_FarhanFamilySuperFund(request):
    return add_item(request, FarhanFamilySuperFundForm)

def add_Ongie(request):
    return add_item(request, OngieForm)

def add_OrangeTrust(request):
    return add_item(request, OrangeTrustForm)


def edit_item(request, pk, model, cls):
    item = get_object_or_404(model, pk=pk)

    if request.method == "POST":
        form = cls(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = cls(instance=item)

        return render(request, 'edit_item.html', {'form': form})



def edit_Farhan(request, pk):
    return edit_item(request, pk, Farhan, FarhanForm)


def edit_Nadia(request, pk):
    return edit_item(request, pk, Nadia, NadiaForm)


def edit_FarhanFamilySuperFund(request, pk):
    return edit_item(request, pk, FarhanFamilySuperFund, FarhanFamilySuperFundForm)

def edit_Ongie(request, pk):
    return edit_item(request, pk, Ongie, OngieForm)

def edit_OrangeTrust(request, pk):
    return edit_item(request, pk, OrangeTrust, OrangeTrustForm)


def delete_Farhan(request, pk):

    template = 'index.html'
    Farhan.objects.filter(id=pk).delete()

    items = Farhan.objects.all()

    context = {
        'items': items,
    }

    return render(request, template, context)


def delete_Nadia(request, pk):

    template = 'index.html'
    Nadia.objects.filter(id=pk).delete()

    items = Nadia.objects.all()

    context = {
        'items': items,
    }

    return render(request, template, context)


def delete_FarhanFamilySuperFund(request, pk):

    template = 'index.html'
    FarhanFamilySuperFund.objects.filter(id=pk).delete()

    items = FarhanFamilySuperFund.objects.all()

    context = {
        'items': items,
    }

    return render(request, template, context)


def delete_Ongie(request, pk):

    template = 'index.html'
    Ongie.objects.filter(id=pk).delete()

    items = Ongie.objects.all()

    context = {
        'items': items,
    }

    return render(request, template, context)

def delete_OrangeTrust(request, pk):

    template = 'index.html'
    OrangeTrust.objects.filter(id=pk).delete()

    items = OrangeTrust.objects.all()

    context = {
        'items': items,
    }

    return render(request, template, context)


