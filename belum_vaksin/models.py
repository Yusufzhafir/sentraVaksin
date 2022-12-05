from django.db import models
import uuid
from datetime import date
from jadwal.models import SesiVaksinasi

# Create your models here.
class PesertaVaksin(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    sesi = models.ForeignKey(SesiVaksinasi, on_delete=models.CASCADE)

    # yang nanti bakal otomatis terisi di form dan tidak bisa diedit
    waktu = models.DateField(("Waktu"), default=date.today)
    tempat_pelaksanaan = models.CharField(max_length=100)
    jenis_vaksin = models.CharField(max_length=20)
    # yang harus diisi di form
    nama_peserta = models.TextField(max_length=100, default="")
    nik = models.TextField(max_length=100, default="")
    no_telp = models.TextField(max_length=100, default="")
    token = models.TextField(max_length=5)

    def __str__(self):
        return self.tempat_pelaksanaan

    
