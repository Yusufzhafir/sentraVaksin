from django.db import models
from django.db.models.deletion import CASCADE
from belum_vaksin.models import PesertaVaksin

# Create your models here.
class EfekSamping(models.Model):
    nama = models.CharField(max_length=20)
    nik = models.BigIntegerField()
    no_hp = models.BigIntegerField()
    alamat = models.TextField()
    
    vaksin = models.CharField(max_length=20)
    gejala = models.TextField()
    token = models.CharField(max_length=5,default="")

    peserta = models.ForeignKey(PesertaVaksin, on_delete=CASCADE)
    
    def __str__(self):
        return self.nama