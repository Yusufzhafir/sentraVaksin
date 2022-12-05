from django.contrib.auth import decorators, login
from django.contrib import messages
from django.http import response
from django.http.response import Http404, HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from jadwal.models import SesiVaksinasi
from jadwal.forms import SesiForm

# Create your views here.
def index(request):
    if not request.user.is_authenticated:
        sesi = SesiVaksinasi.objects.all().values()
        response = {'sesi': sesi}
        return render(request, 'list_sesi_visitor.html', response)
    sesi = SesiVaksinasi.objects.all().values()
    response = {'sesi': sesi}
    return render(request, 'list_sesi_admin.html', response)

def detail_view(request, sesi_id):
    try:
        sesi = SesiVaksinasi.objects.get(pk=sesi_id)
        response = {'sesi' : sesi}
        return render(request, 'detail_sesi.html', response)
    except SesiVaksinasi.DoesNotExist:
        raise Http404("Objek tidak ditemukan")
    
    
@login_required()
def add_sesi(request):
    form = SesiForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect('../jadwal')
    
    response = {'form' : form}
    return render(request, 'form_sesi.html', response)

@login_required
def edit_sesi(request, sesi_id):
    try:
        sesi = SesiVaksinasi.objects.get(pk=sesi_id)
    except SesiVaksinasi.DoesNotExist:
        raise Http404("Objek tidak ditemukan")
    form = SesiForm(request.POST or None, instance=sesi)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect('../../jadwal')
    
    response = {'form' : form}
    return render(request, 'form_sesi.html', response)

@login_required
def delete_sesi(request, sesi_id):
    try:
        sesi = SesiVaksinasi.objects.get(pk=sesi_id)
        sesi.delete()
        messages.success(request, 'Sukses Menghapus Task.')
        return HttpResponseRedirect('../../jadwal')
    except SesiVaksinasi.DoesNotExist:
        raise Http404("Objek tidak ditemukan")

    

    


