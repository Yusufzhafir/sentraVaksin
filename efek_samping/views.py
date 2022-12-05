from django.contrib.auth import login
from django.shortcuts import render
from .models import EfekSamping
from django.http.response import HttpResponse
from django.http import response, HttpResponseRedirect
from django.core import serializers
from .forms import EfekSampingForm
from belum_vaksin.models import PesertaVaksin
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def laporan(request):
    
    response = {}
    return render(request, 'laporan.html', response)

def lapor(request):
    form = EfekSampingForm(request.POST or None)
    peserta_vaksin = PesertaVaksin.objects.all()
    
    if (form.is_valid() and request.method == 'POST'):
        token_valid = False
        
        laporan = form.save(commit=False)
        for peserta in peserta_vaksin:
            if laporan.token == peserta.token:
                laporan.peserta = peserta # add foreign key relations
                token_valid = True
        
        if token_valid:
            form.save()
            messages.info(request,"Data berhasil disimpan")
            return HttpResponseRedirect('/efek-samping/lapor')
        else:
            messages.info(request,"Maaf token Anda salah")
            return HttpResponseRedirect('/efek-samping/lapor')
        
    response = {'form':form}
    return render(request, 'lapor.html', response)

def json(request):
    data = serializers.serialize('json', EfekSamping.objects.all())
    return HttpResponse(data, content_type="application/json")