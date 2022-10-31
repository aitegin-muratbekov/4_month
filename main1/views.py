from django.shortcuts import render, HttpResponse, redirect
from datetime import date
from main1.models import Film, Director, Comments
from .forms import FilmForm, DirectorForm, UserCreateForm, UserLoginForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout



# Create your views here.
def logout_view(request):
    logout(request)
    return redirect('/index/')

def login_view(request):
    context= {
        'form': UserLoginForm()
    }
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(username=username, password=password)
            if not user:
                return redirect('/login/')
            else:
                login(request, user)
                return redirect('/index/')
    return render(request, 'login.html', context)
def register_view(request):
    context = {
        'form': UserCreateForm
    }
    if request.method == 'POST':
        form = UserCreateForm(data=request.POST)
        if form.is_valid():
           username = request.POST.get('username')
           password = request.POST.get('password')
           User.objects.create_user(username=username, password=password)

           return redirect('/login/')
        context['form'] = form

    return render(request, 'register.html', context=context)

def film_create_view(request):
    context = {
        'form': FilmForm()
    }

    if request.method == 'POST':
        form = FilmForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('/films/')
    return render(request, 'create.html', context)


def director_create_view(request):
    context = {
        'form': DirectorForm()
    }

    if request.method == 'POST':
        form = DirectorForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('/directors/')
    return render(request, 'create_d.html', context)

def film_detail_view(request, id):
    dict_ = {}
    film = Film.objects.get(id=id)
    dict_['film_detail'] = film
    dict_['comm_list'] = Comments.objects.filter(film_id=film)
    return render(request, 'detail.html', context=dict_)


def index_view(request):
    print(request.user)
    return render(request, 'index.html')


def about_us_view(request):
    return render(request, 'about_us.html')


def date_now(request):
    data = date.today()
    dict = {
        'data': data,
    }
    return render(request, 'time.html', context=dict)

PAGE_SIZE = 3

def film_list_view(request):
    page = int(request.GET.get('page', 1))
    film_list = Film.objects.all()[PAGE_SIZE * (page-1): PAGE_SIZE*page]
    dict_ = {
        'previous_page': page-1,
        'next_page': page+1,
        'film_list': film_list,
        'pages': list(range(1, len(Film.objects.all()) // PAGE_SIZE + 2))
    }
    return render(request, 'films.html', context=dict_)


def directors_view(request):
    dict_ = {
        'director_list': Director.objects.all()
    }
    return render(request, 'directors.html', context=dict_)


def director_detail_view(request, id):
    dict_ = {}
    director = Director.objects.get(id=id)
    dict_['director'] = director
    dict_['film_list'] = Film.objects.filter(film_director=director)

    return render(request, 'director_detail.html', context=dict_)


def search_view(request):
    search_word = request.GET.get('search_word', '')
    context = {
        'films': Film.objects.filter(title__icontains=search_word).order_by('-comments', 'title').exclude(rating=0),
        'search_word': search_word

    }
    return render(request, 'search.html', context)