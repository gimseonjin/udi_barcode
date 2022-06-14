"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth.views import LogoutView
from django.urls import path


from barcode_server.views import login_view, register_user, index, user_page, logout_view, dashboard

urlpatterns = [
    path('admin/', admin.site.urls),
    # The home page
    path('', index, name='home'),
    path('dashboard/', dashboard, name='dashboard'),
    path('user/', user_page, name='user_page'),
    path("login/", login_view, name="login"),
    path("register/", register_user, name="register"),
    path("logout/", logout_view, name="logout")
]
