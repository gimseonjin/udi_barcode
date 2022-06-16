"""
This is Views(business logic) in Barcode_server
"""
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile

from barcode_server.forms import LoginForm, SignUpForm, UploadFileForm
from barcode_server.models import Result, User
from barcode_server.service.barcode_service import BarcodeService

# Create your views here.


@login_required(login_url="/login/")
def index(request):
    '''
    Title : index

    This is index, main page view

    This page do recognize barcode logic

    return:
        GET : return home/index.html
        POST : return home/index.html with result
    '''
    context = {'segment': 'index'}
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            f = request.FILES["file"]
            user_one = User.objects.filter(user_id=request.user.id).first()
            path = default_storage.save('static/media/barcode.jpeg', ContentFile(f.read()))
            barcodeService = BarcodeService()
            msg = barcodeService.uploadSerivce(path)
            result = Result(user=user_one,recognized=msg.get("msg"),udi=msg.get("data"),img_path="/"+path)
            result.save()
            context["msg"] = msg.get("msg")
            context["data"] = msg.get("data")
            return render(request, 'home/index.html', context)
    else:
        form = UploadFileForm()
    return render(request, 'home/index.html', context)


@login_required(login_url="/login/")
def dashboard(request):
    '''
    Title : dashboard

    This is dashboard view

    This page return histories

    return:
        All : return home/dashboard.html
    '''
    results = Result.objects.filter(user_id = request.user.id).all().order_by('-dates')[:10]
    context = {'segment': 'dashboard', "results" : results}
    return render(request, 'home/dashboard.html', context)


@login_required(login_url="/login/")
def user_page(request):
    '''
    TODO : Add update user date form!

    Title : user_page

    This is user_page view

    This page return user data

    return:
        All : return home/page-user.html
    '''
    context = {'segment': 'user'}
    return render(request, 'home/page-user.html', context)

def login_view(request):
    '''
    Title : login_view

    This is login view

    It has login form to login logic

    return:
        GET : return home/dashboard.html
        POST : return home/dashboard.html with result of login
    '''
    form = LoginForm(request.POST or None)
    msg = None
    if request.method == "POST":
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("/")
            msg = 'Invalid credentials'
        else:
            msg = 'Error validating the form'
    return render(request, "accounts/login.html", {"form": form, "msg": msg})


def register_user(request):
    '''
    Title : register_user

    This is register view

    It has register form to register logic

    return:
        GET : return accounts/register.html
        POST :
            if sueccess :
                redirect "/"
            else :
                return accounts/register.html with fail
    '''
    msg = None
    success = False
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            admin_user=form.save()
            user = User(user=admin_user)
            user.save()
            username = form.cleaned_data.get("username")
            raw_password = form.cleaned_data.get("password1")
            authenticate(username=username, password=raw_password)
            msg = 'User created - please <a href="/login">login</a>.'
            success = True
        else:
            msg = 'Form is not valid'
    else:
        form = SignUpForm()
    return render(request, "accounts/register.html", {"form": form, "msg": msg, "success": success})


def logout_view(request):
    '''
    Title : logout_view

    This is logout view

    return:
        All : redirect login page
    '''
    logout(request)
    return redirect("login")
