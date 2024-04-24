from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from django.http import JsonResponse
from .forms import *
from django.core import serializers
from django.contrib.auth.decorators import login_required
from users.utils import *

@login_required
def edinica_list(request):
    edinica_list = Edinica.objects.all()
    return render(request, 'inventory/list.html', {'edinica_list': edinica_list})

@login_required
def sklads_list(request):
    sklads = Sklads.objects.all()  # Получаем все склады
    return render(request, 'inventory/sklads.html', {'sklads': sklads})

@login_required
def sklads_floors(request, sklads_id):
    sklads = Sklads.objects.get(id=sklads_id)  # Получаем конкретный склад по его ID
    etazh = Etazh.objects.filter(sklad=sklads)  # Получаем все этажи на этом складе
    return render(request, 'inventory/sklads_etazh.html', {'sklads': sklads, 'etazh': etazh})

@login_required
def floor_cabinets(request, etazh_id):
    etazh = Etazh.objects.get(id=etazh_id)  # Получаем конкретный этаж по его ID
    kabinets = Kabinet.objects.filter(etazh=etazh)  # Получаем все кабинеты на этом этаже
    return render(request, 'inventory/floor_cabinets.html', {'etazh': etazh, 'kabinets': kabinets})

@login_required
def cabinet_units(request, kabinet_id):
    kabinet = Kabinet.objects.get(id=kabinet_id)  # Получаем конкретный кабинет по его ID
    units = Edinica.objects.filter(kabinet=kabinet)  # Получаем все единицы техники в этом кабинете
    return render(request, 'inventory/cabinet_units.html', {'kabinet': kabinet, 'units': units})

@login_required
def edinica_detail(request, pk):
    edinica_detail = get_object_or_404(Edinica, pk=pk)
    context = {'edinica_detail': edinica_detail}
    return render(request, 'inventory/detail.html', context)

@login_required
def create_edinica(request):
    if request.method == 'POST':
        form = EdinicaForm(request.POST)
        if form.is_valid():
            new_object=form.save() 
            add_object(request, new_object) # Сохранить данные в базе данных
            return redirect('storage:sklads_list')
        else:
            errors = form.errors.as_json()
            return JsonResponse({'success': False, 'errors': errors})
    else:
        form = EdinicaForm()
        sklad_list = Sklads.objects.all()  # Получить список складов
        return render(request, 'inventory/create.html', {'form': form, 'sklad_list': sklad_list})

@login_required
def edit_edinica(request, edinica_id):
    edinica = get_object_or_404(Edinica, pk=edinica_id)
    if request.method == 'POST':
        form = EdinicaForm(request.POST, instance=edinica)
        if form.is_valid():
            new_object = form.save()  # Сохранить изменения
            edit_object(request, new_object)
            return redirect('storage:sklads_list')
    else:
        form = EdinicaForm(instance=edinica)
        sklad_list = Sklads.objects.all()  # Получить список складов
        return render(request, 'inventory/edit.html', {'form': form, 'sklad_list': sklad_list})

@login_required
def delete_edinica(request, edinica_id):
    edinica_detail = get_object_or_404(Edinica, pk=edinica_id)
    if request.method == 'POST':
        delete_object(request, edinica_detail)
        edinica_detail.delete()
        return redirect('storage:sklads_list')  # Перенаправляем на главную страницу
    elif request.method == 'GET':
        # Если метод запроса GET, просто отобразите страницу с подтверждением удаления или другое действие
        return render(request, 'inventory/detail.html', {'edinica_detail': edinica_detail})



def get_floors(request):
    sklad_id = request.GET.get('sklad_id')
    etazh_list = Etazh.objects.filter(sklad_id=sklad_id).values('id', 'title')
    return JsonResponse({'etazh_list': list(etazh_list)})

def get_rooms(request):
    etazh_id = request.GET.get('etazh_id')
    kabinet_list = Kabinet.objects.filter(etazh_id=etazh_id).values('id', 'title')
    return JsonResponse({'kabinet_list': list(kabinet_list)})

