import datetime
from django.core.paginator import Paginator
from django.shortcuts import render
from django.http import HttpResponse

menu = ['Главая страница', 'Время', 'Содержимое сайта']

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
}



def omlet(request, recipe):
    if recipe in DATA.keys():
        servings = request.GET.get('servings', 1)
        ingridients = {}
        for ingridient in DATA[recipe]:
            ingridients[ingridient] = round(DATA[recipe][ingridient] * int(servings), 2)
        context = {
            'recipe': ingridients
        }
    else:
        context = {}
    return render(request, 'mytestsite/index.html', context)

'''

Предыдущая др

'''


def test_view(request):
    return render(request, 'mytestsite/package.html', {'title': 'Главная страница'})


def current_time(request):
    return HttpResponse(f'Time = {datetime.datetime.now()},')


def workdir(request):
    return render(request, 'mytestsite/workdir.html', {'menu': menu, 'title': 'Содержимое сайта'})
