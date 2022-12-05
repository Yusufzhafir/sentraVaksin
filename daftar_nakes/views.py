from django.shortcuts import render
from .models import nakes
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required()
def index(request):
    Nakes = nakes.objects.all().values()
    response = {'Nakes': Nakes}
    # response = {}
    form = nakesForm(request.POST or None, request.FILES or None)
    response['form']= form
    if (request.method=='POST')&(form.is_valid())&request.is_ajax():
        # check if form data is valid
        # nakes_baru = form.save(commit=False)
        # nakes_baru.id = nakes.objects.get(nama=form['nama'][0]).id
        # nakes_baru.save()
        # form.save_m2m()
        form.save()
        nakes_baru = nakes.objects.get(nama=form['nama'].value())
        response_ajax = {'id':nakes_baru.id,'nama':nakes_baru.nama,'umur':nakes_baru.umur,
        'rumah_sakit':nakes_baru.rumah_sakit,'pendidikan':nakes_baru.pendidikan}
        return JsonResponse(response_ajax)

    else:
        return render (request,'daftar_nakes.html',response)

@login_required()
def delete_nakes(request,nakes_id):
    try:
        tenaga = nakes.objects.get(pk=nakes_id)
        tenaga.delete()
        messages.success(request, 'Sukses Menghapus Task.')
        return HttpResponseRedirect('/daftar_nakes')
    except nakes.DoesNotExist:
        raise Http404("Objek tidak ditemukan")
# def add_nakes(request):
#     response = {}
#     form = nakesForm(request.POST or None, request.FILES or None)
#     response['form']= form
#     if (request.method=='POST')&(form.is_valid()):
#         # check if form data is valid
#         form.save()
#         return render (request,'daftar_nakes.html',response)
#         # Redirect to a success page.
#     else:
#         return render (request,'daftar_nakes.html',response)

# response_ajax = json.dumps(response)
# json_serializer = serializers.get_serializer("json")()
# response = json_serializer.serialize(response_ajax, ensure_ascii=False)
# return JsonResponse(json.loads(response))
# return HttpResponse(response, mimetype="application/json") 
# return render (request,'daftar_nakes.html',response)
# json_serializer = serializers.get_serializer("json")()
# response = json_serializer.serialize(response_ajax, ensure_ascii=False)
# (request.headers.get('x-requested-with') == 'XMLHttpRequest')
