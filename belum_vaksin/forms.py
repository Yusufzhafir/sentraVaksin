from django import forms
from belum_vaksin.models import PesertaVaksin

class RegisterForm(forms.ModelForm):
    class Meta:
        model = PesertaVaksin
        fields = ['waktu', 'tempat_pelaksanaan', 'jenis_vaksin', 'nama_peserta', 'nik', 'no_telp']
    
    nama_peserta = forms.CharField(max_length=100, required=True)
    nik = forms.CharField(max_length=100, required=True)
    no_telp = forms.CharField(max_length=100, required=True)

    waktu = forms.DateField(label='Waktu:', required=True, widget=forms.DateInput(attrs={'readonly':'readonly'}))
    tempat_pelaksanaan = forms.CharField(label='Tempat pelaksanaan:', required=True, widget=forms.TextInput(attrs={'readonly':'readonly'}))
    jenis_vaksin = forms.CharField(label='Jenis vaksin:', required=True, widget=forms.TextInput(attrs={'readonly':'readonly'}))
