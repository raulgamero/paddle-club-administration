"""
URL configuration for padel_club_administration project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path
from padel_admin import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.landing, name='landing'),
    path('reserves/', views.lista_reserves, name='lista_reserves'),
    path('jugadors/', views.lista_jugadors, name='lista_jugadors'),
    path('cobrament/<str:data>/<str:id_jugador>', views.lista_cobraments, name='lista_cobraments'),
    path('logout/', views.logout, name='logout')
]
