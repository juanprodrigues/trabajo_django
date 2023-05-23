from django import forms
from .models import Trabajador, Oficio, Contacto
TYPE_CHOICES = [
    ("consulta", "Consulta"),
    ("reclamo","Reclamo"),
    ("sugerencia", "Sugerencia")
]

OFICIO = [
      ("electricista", "Electricista"),
      ("plomero", "Plomero"),
      ("cerrajero", "Cerrajero"),
      ("albañil", "Albañil"),

]

class TrabajadorForm(forms.ModelForm):
    fecha_nacimiento = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    clave = forms.CharField(widget=forms.PasswordInput)
    oficio = oficio = forms.ModelChoiceField(queryset=Oficio.objects.all())
    class Meta:
        model = Trabajador
        fields = '__all__'
    

class ContactoForm(forms.ModelForm):
    tipo = forms.ChoiceField(choices= TYPE_CHOICES)
    fecha_consulta = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    mensaje = forms.CharField(label= "Mensaje", widget=forms.Textarea(attrs={'class':'area_texto'}))
    class Meta: 
        model = Contacto   
        fields = '__all__'
    