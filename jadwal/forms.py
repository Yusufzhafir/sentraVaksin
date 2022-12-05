from django import forms
from jadwal.models import SesiVaksinasi

class SesiForm(forms.ModelForm):
    class Meta:
        model = SesiVaksinasi
        fields = ['waktu', 'tempat_pelaksanaan', 'jenis_vaksin', 'kuota']

    waktu = forms.DateField(label='Waktu:', required=True, widget=forms.DateInput(attrs={'type': 'date'}))
    tempat_pelaksanaan = forms.CharField(label='Tempat pelaksanaan:', required=True, widget=forms.TextInput(attrs={'type': 'text'}))
    jenis_vaksin = forms.CharField(label='Jenis vaksin:', required=True, widget=forms.TextInput(attrs={'type': 'text'}))
    kuota = forms.IntegerField(label="Kuota:", required=True, widget=forms.NumberInput(attrs={'type': 'text'}))