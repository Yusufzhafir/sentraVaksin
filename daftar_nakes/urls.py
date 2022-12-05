from django.urls import path
from .views import  index

urlpatterns = [
    path('', index, name='index')
    # path('add_sesi/', add_sesi, name='add_sesi')
]
