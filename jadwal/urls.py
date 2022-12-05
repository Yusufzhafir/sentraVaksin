from django.urls import path
from .views import add_sesi, delete_sesi, index, detail_view, edit_sesi, delete_sesi

urlpatterns = [
    path('', index, name='index'),
    path('add_sesi', add_sesi, name='add_sesi'),
    path('<sesi_id>', detail_view, name='detail_view'),
    path('edit_sesi/<sesi_id>', edit_sesi, name='edit_sesi'),
    path('delete_sesi/<sesi_id>', delete_sesi, name='delete_sesi'),
]
