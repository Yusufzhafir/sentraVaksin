from django.urls import path
from dummy.views import get_user_list, register_request, login_request, logout_request
from home.views import index

urlpatterns = [
    path('', index, name='index'),
    path('home', index, name='index'),
    path("alpha", register_request, name="alpha"),
    path("lambda", login_request, name="lambda"),
    path("zeus", get_user_list, name="zeus"),
    path("omega", logout_request, name="omega")
]