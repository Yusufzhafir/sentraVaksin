from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import  render, redirect
from dummy.forms import NewUserForm
from django.contrib.auth import get_user_model, login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    return render(request, 'coming_soon.html')

@login_required
def get_user_list(request):
    users = get_user_model().objects.all()
    response = {'users': users}
    return render(request, 'zeus.html', response)


def register_request(request):
    if request.method == "POST":
	    form = NewUserForm(request.POST or None)
	    if form.is_valid():
		    user = form.save()
		    login(request, user)
		    messages.success(request, "Registrasi berhasil." )
		    return HttpResponseRedirect('/zeus')
	    messages.error(request, "Registrasi gagal. Informasi invalid")
    else:
        form = NewUserForm()
        return render (request, "alpha.html", {"form":form})

def login_request(request):
    if request.method == "POST":
	    form = AuthenticationForm(request, data=request.POST)
	    if form.is_valid():
		    username = form.cleaned_data.get('username')
		    password = form.cleaned_data.get('password')
		    user = authenticate(username=username, password=password)

		    if user is not None:
		        login(request, user)
		        messages.info(request, f"Berhasil login sebagai {username}.")
		        return HttpResponseRedirect('/zeus')
		    else:
		        messages.error(request,"Gagal login, username atau password invalid.")

	    else:
		    messages.error(request,"Gagal login, username atau password invalid.")

    form = AuthenticationForm()
    return render(request, "lambda.html", {"form":form})

@login_required
def logout_request(request):
    logout(request)
    messages.info(request, "Berhasil log out.")
    return HttpResponseRedirect('/home')
