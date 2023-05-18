import sqlite3

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

from .forms import CartoonUserForm
from .models import CartoonUser, Cartoon

con = sqlite3.connect('db.sqlite3', check_same_thread=False)
redirect_link = '/'
user = None
cartoon = None


def get_info_numb(request, sign_path: int):
    """This method checks if number in url"""
    return HttpResponse(f"<h3>Incorrect path: {sign_path}</h3>")


def index(request):
    """Endpoint with fields for login"""
    return render(request, 'nickelodeon/index.html')


def login(request):
    """Home page after user logs in"""
    if request.POST:
        form_data = CartoonUserForm(request.POST)
        if form_data.is_valid():
            username = form_data.cleaned_data['username']
            surname = form_data.cleaned_data['surname']
            global user
            user = CartoonUser(username, surname)
            CartoonUser.objects.create(username=username, surname=surname)
            template = 'nickelodeon/login.html'
        return render(request, 'nickelodeon/login.html', {"user": user, "error_message": form_data.errors})
    else:
        return HttpResponseRedirect(redirect_link)


def add_cartoon(request):
    """Endpoint for adding Cartoons title"""
    if user:
        template = 'nickelodeon/add_cartoon_title.html'
        return render(request, template, {"user": user})
    else:
        return HttpResponseRedirect(redirect_link)


def add_cartoon_info(request):
    """Endpoint for adding all information about added cartoon"""
    cartoon_title = request.POST.get('cartoon_title')
    global cartoon
    cartoon = Cartoon(title=cartoon_title)
    add_user = Cartoon(title=cartoon_title)
    add_user.save()
    template = 'nickelodeon/add_cartoon_info.html'
    return render(request, template, {"title": cartoon_title})


def show_info(request):
    """Show all information about added cartoon"""
    if cartoon:
        year = request.POST.get('cartoon_year')
        author = request.POST.get('cartoon_author')
        rating = request.POST.get('cartoon_rating')
        upd_cartoon = Cartoon.objects.filter(title=cartoon.title).update(year=year, author=author, rating=rating)
        template = 'nickelodeon/show_info.html'
        cartoon_info = Cartoon.objects.get(title=cartoon.title)
        return render(request, template, {"cartoon": cartoon_info})
    else:
        return HttpResponseRedirect(redirect_link)


def all_info_from_db(request):
    cartoons = Cartoon.objects.all()
    template = 'nickelodeon/all_info_from_db.html'
    return render(request, template, {'cartoons': cartoons})
