from django.shortcuts import render, HttpResponse
from datetime import date
from main1.models import Film, Director
# Create your views here.
def film_detail_view(request, id):
    dict_ = {}
    film = Film.objects.get(id=id)
    dict_['film_detail'] = film

    return render(request, 'detail.html', context= dict_)



def index_view(request):
    return render(request, 'index.html')
def about_us_view(request):
    return render(request, 'about_us.html')

def date_now(request):
    data = date.today()
    dict = {
       'data' : data,
    }
    return render(request, 'time.html', context=dict)


def film_list_view(request):
    dict_ = {
        'film_list' : Film.objects.all()
    }
    return render(request, 'films.html', context=dict_)


def directors_view(request):
    dict_ = {
        'director_list' : Director.objects.all()
    }
    return render(request, 'directors.html', context=dict_)


def director_detail_view(request, id):
    dict_ = {}
    director = Director.objects.get(id=id)
    dict_['director'] = director
    dict_['film_list'] = Film.objects.filter(film_director=director)


    return render(request, 'director_detail.html', context=dict_)