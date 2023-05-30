from django.shortcuts import render
import json



def home(request):
    return render(request, 'index.html')


def countries_list(request):
    with open ('country.json', 'r') as my_file:
        countries_json = my_file.read()
    countries_json_list = json.loads(countries_json)
    context = {
        'countries' : countries_json_list,
    }
    return render(request, 'countries_list.html', context)


def country_page(request, str):
    with open ('country.json', 'r') as my_file:
        countries_json = my_file.read()
    countries_json_list = json.loads(countries_json)
    for country in countries_json_list:
        if str == country['country']:
            country_dict = country
            context = {
                        'countries_dict' : country_dict,
            }
            break
    return render(request, 'country_page.html', context)


def languages_list(request):
    with open ('country.json', 'r') as my_file:
        countries_json = my_file.read()
    countries_json_list = json.loads(countries_json)
    languages_list = []
    for country in countries_json_list:
        for language in country['languages']:
            languages_list.append(language)
    languages_list.sort()
    languages_list = set(languages_list)
    context = {
        'languages_list' : languages_list
    }
    return render(request, 'languages.html', context)