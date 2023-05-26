from datetime import datetime
from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Jugadors, Reserva, Cobrament

def landing(request):
    return render(request, 'landing.html')

def lista_reserves(request):
    fecha = request.GET.get('fecha')
    if fecha:
        fecha = datetime.strptime(fecha, '%Y-%m-%d').date()
        reserves = Reserva.objects.filter(data=fecha)
    else:
        reserves = Reserva.objects.all()
    return render(request, 'lista_reserves.html', {'reserves': reserves})

def lista_jugadors(request):
    search_query = request.GET.get('search')
    
    if request.method == 'POST':
        # Procesar los datos del formulario
        nom = request.POST.get('nom')
        cognom = request.POST.get('cognom')
        email = request.POST.get('email')
        telefon = request.POST.get('telefon')
        nivell = request.POST.get('nivell')
        contrasenya = 'a'

        jugador = Jugadors(nom=nom, cognom=cognom, email=email, telefon=telefon, nivell=nivell, contrasenya=contrasenya)
        jugador.save()

    '''if request.method == 'PUT':
        # Procesar los datos del formulario
        nom = request.PUT.get('nom')
        cognom = request.PUT.get('cognom')
        email = request.PUT.get('email')
        telefon = request.PUT.get('telefon')
        nivell = request.PUT.get('nivell')
        contrasenya = 'a'

        jugador = Jugadors(nom=nom, cognom=cognom, email=email, telefon=telefon, nivell=nivell, contrasenya=contrasenya)
        jugador.save()'''
    
    if request.method == 'DELETE':
        jugador = Jugadors.objects.get(id=request.DELETE.get('jugador_id'))
        jugador.delete()

    jugadors_list = Jugadors.objects.all()
    
    if search_query:
        jugadors_list = jugadors_list.filter(nom__icontains=search_query) | jugadors_list.filter(cognom__icontains=search_query)
    
    paginator = Paginator(jugadors_list, 100)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'page_obj': page_obj,
        'search_query': search_query,
    }
    
    return render(request, 'lista_jugadors.html', context)


def lista_cobraments(request):
    cobraments = Cobrament.objects.all()
    return render(request, 'lista_cobraments.html', {'cobraments': cobraments})