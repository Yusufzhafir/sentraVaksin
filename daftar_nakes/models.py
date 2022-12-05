from django.db import models
import uuid
from jadwal.models import SesiVaksinasi

# Create your models here.
class nakes(models.Model):
    nama = models.CharField(max_length=30)
    umur = models.IntegerField()
    rumah_sakit = models.CharField(max_length=30)
    pendidikan = models.CharField(max_length=30)

    # Developing relations to Jadwal
    #sesi = models.ForeignKey(SesiVaksinasi, on_delete=models.CASCADE, null=True)

    def __str__(self) -> str:
        return self.nama