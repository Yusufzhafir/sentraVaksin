from django import forms
from .models import nakes
from jadwal.models import SesiVaksinasi

class nakesForm (forms.ModelForm):
    class Meta:
        model = nakes
        fields = "__all__"
    
    # sesi = forms.ModelChoiceField(queryset=SesiVaksinasi.objects.all())
