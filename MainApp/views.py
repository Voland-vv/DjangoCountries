from django.shortcuts import render
from MainApp.models import Country, Language
import json



def home(request):
    return render(request, 'index.html')


def countries_list(request):
    countries = Country.objects.all()
    context = {
        'countries' : countries,
    }
    return render(request, 'countries_list.html', context)


def country_page(request, str):
    country = Country.objects.get(name=str)
    languages = country.languages.all()
    context = {
        'country' : country,
        'languages' : languages
    }
    return render(request, 'country_page.html', context)


def languages_list(request):
    languages = Language.objects.all()
    context = {
        'languages' : languages
    }
    return render(request, 'languages.html', context)