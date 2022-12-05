import random
from django import http
from django.http import response
from django.http.response import Http404, HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.core import serializers
from django.http import JsonResponse
from django.shortcuts import redirect

from belum_vaksin.models import PesertaVaksin
from belum_vaksin.forms import RegisterForm
from jadwal.models import SesiVaksinasi

# Create your views here.

@login_required(login_url='pilih_jadwal') # untuk visitor
def index(request):
    # untuk admin:
    return render(request, 'index_admin.html')

# untuk visitor:
def pilih_jadwal(request):
    return render(request, 'belum_pilih_jadwal.html')

def generate_token():
        chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890";
        chars_list=[]
        for char in chars:
            chars_list.append(char);
        
        token = ""
        for i in range(5):
            token += random.choice(chars_list)

        return token

def register_vaksin(request, sesi_id):
    try:
        sesi = SesiVaksinasi.objects.get(pk=sesi_id)
        if (sesi.kuota <= 0):
            raise Http404("Mohon maaf, kuota untuk sesi ini sudah habis...")

        init = {'waktu':sesi.waktu, 'tempat_pelaksanaan':sesi.tempat_pelaksanaan, 'jenis_vaksin':sesi.jenis_vaksin}
        form = RegisterForm(request.POST or None, initial = init)
        
        if form.is_valid():
            pesertaBaru = form.save(commit=False)
            pesertaBaru.sesi = sesi
            pesertaBaru.token = generate_token()
            pesertaBaru.save()
            form.save_m2m()

            sesi.kuota = sesi.kuota - 1
            sesi.save()

            response = {'peserta': pesertaBaru}
            return render(request, 'konfirmasi_registrasi.html', response)
    
        response = {'form' : form}
        return render(request, 'form_register.html', response)
        
    except SesiVaksinasi.DoesNotExist:
        raise Http404("Jadwal tidak ditemukan!")
    
    

# untuk admin:
@login_required()
def list_peserta(request):
    jmlPeserta = PesertaVaksin.objects.all().count()
    peserta = PesertaVaksin.objects.all().values()
    # untuk load more
    paginator=Paginator(peserta, 5)
    page_number=request.GET.get('page')
    posts_obj=paginator.get_page(page_number)
    if jmlPeserta != 0:
        return render(request,'list_peserta.html', {'posts':posts_obj, 'jmlPeserta' : jmlPeserta})
    else:
        return render(request, 'belum_ada_peserta.html')

@login_required()
def load_more(request):
    offset=int(request.POST['offset'])
    limit = 5
    posts=PesertaVaksin.objects.all()[offset:limit+offset]
    totalData=PesertaVaksin.objects.count()
    data={}
    posts_json=serializers.serialize('json',posts)
    return JsonResponse(data={
        'posts':posts_json,
        'totalResult':totalData
    })

@login_required()
def delete_peserta(request, peserta_id):
    try:
        peserta = PesertaVaksin.objects.get(pk=peserta_id)
        peserta.delete()
        return HttpResponseRedirect('../list_peserta')
    except PesertaVaksin.DoesNotExist:
        raise Http404("Peserta tidak ditemukan!")
