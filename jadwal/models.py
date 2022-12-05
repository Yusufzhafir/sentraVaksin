import uuid
from django.db import models
from datetime import date

# Create your models here.
class SesiVaksinasi(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    waktu = models.DateField(("Waktu"), default=date.today)
    tempat_pelaksanaan = models.CharField(max_length=100)
    jenis_vaksin = models.CharField(max_length=20)
    kuota = models.IntegerField(default=0)

    def __str__(self):
        return self.waktu