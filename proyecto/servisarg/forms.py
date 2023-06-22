from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import Trabajador, Oficio, ConsultaReclamoSugerencia
from django.core.exceptions import ValidationError
from datetime import date
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.utils import timezone



TYPE_CHOICES = [
    ("Consulta", "Consulta"),
    ("Reclamo", "Reclamo"),
    ("Sugerencia", "Sugerencia")
]

class TrabajadorForm(forms.ModelForm):
    fecha_nacimiento = forms.DateField(widget=forms.DateInput(
        attrs={'type': 'date', 'class': 'form-control'}))
    dni = forms.IntegerField(max_value=999999999, widget=forms.TextInput(
        attrs={'class': 'form-control', 'type': 'number'}))
    oficios = forms.ModelMultipleChoiceField(
        queryset=Oficio.objects.all(),
        widget=forms.CheckboxSelectMultiple(attrs={'class': 'form-check-input'})
    )
    first_name = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control'}), required=True)
    last_name = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control'}), required=True)
    email = forms.EmailField(widget=forms.EmailInput(
        attrs={'class': 'form-control'}), required=True)


    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user')  # Obtener el usuario logeado
        super().__init__(*args, **kwargs)
        self.fields['oficios'].widget.attrs.update({'class': 'form-control'})
        self.user = user  # Asignar el usuario a un atributo de la instancia del formulario
        self.initial['first_name'] = user.first_name
        self.initial['last_name'] = user.last_name
        self.initial['foto'] = user.photo
        
    def save(self, commit=True, request=None):
        instance = super().save(commit=False)
        if Trabajador.objects.filter(username=self.user).exists():
            trabajador_modificar = Trabajador.objects.get(username=self.user)
            if trabajador_modificar:
                instance.id = trabajador_modificar.id
        user = User.objects.get(username=self.user)
        # Establecer el usuario logeado en el campo 'usuario'
        instance.username = user.username
        instance.last_login = user.last_login
        instance.usuario_id = user.id
        instance.password = user.last_login
        if request is not None and 'foto' in request.FILES:
            instance.foto = request.FILES['foto']

        if commit:
            instance.save()
            self.save_m2m()  # Guardar las relaciones many-to-many (oficios)
        return instance

    class Meta:
        exclude = ('usuario', 'user_permissions', 'groups', 'is_active', 'date_joined',
                   'is_staff', 'password', 'last_login', 'is_superuser', 'username')
        model = Trabajador
        fields = '__all__'
        widgets = {

            'direccion': forms.TextInput(attrs={'class': 'form-control'}),
            'telefono': forms.NumberInput(attrs={'class': 'form-control', 'type': 'number'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-select', 'rows': 3, 'style': 'resize: none;'}),

            
        }
    def clean_dni(self):
        dni= self.cleaned_data.get('dni')
        
        if Trabajador.objects.filter(dni=dni).exists():
            raise forms.ValidationError(
                "Ya existe un Usuario con este DNI"
            )
            
        return dni
        
    def clean_email(self):
        email = self.cleaned_data.get('email')

        # Verificar si ya existe un trabajador con este correo electrónico
        if Trabajador.objects.filter(email=email).exists():
            raise forms.ValidationError(
                "Ya existe un Usuario con este correo electrónico.")

        return email

    def clean_fecha_nacimiento(self):
        fecha_nacimiento = self.cleaned_data.get('fecha_nacimiento')

        # Verificar si la fecha de nacimiento es válida
        if fecha_nacimiento:
            # Obtener la fecha actual
            fecha_actual = date.today()

            # Calcular la edad a partir de la fecha de nacimiento
            edad = fecha_actual.year - fecha_nacimiento.year - ((fecha_actual.month, fecha_actual.day) <
                 (fecha_nacimiento.month, fecha_nacimiento.day))

            # Verificar si la edad es menor a 18 años (mayor de edad)
            if edad <18:
                raise forms.ValidationError("Debes ser mayor de edad para registrarte.")
        
        return fecha_nacimiento   



class TrabajadorModificarForm(forms.ModelForm):
    fecha_nacimiento = forms.DateField(widget=forms.DateInput(
        attrs={'type': 'date', 'class': 'form-control'}))
    dni = forms.IntegerField(max_value=999999999, widget=forms.TextInput(
        attrs={'class': 'form-control', 'type': 'number'}))
    oficios = forms.ModelMultipleChoiceField(
        queryset=Oficio.objects.all(),
        widget=forms.CheckboxSelectMultiple(attrs={'class': 'form-check-input'}),
        required=False
    )
    first_name = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control'}), required=True)
    last_name = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control'}), required=True)
    email = forms.EmailField(widget=forms.EmailInput(
        attrs={'class': 'form-control'}), required=True)
    def clean(self):
        cleaned_data = super().clean()
        oficios = cleaned_data.get('oficios')
        if not oficios:
            self.add_error('oficios', 'Debe seleccionar al menos un oficiog.')

    class Meta:
        exclude = ('usuario', 'user_permissions', 'groups', 'is_active', 'date_joined',
                   'is_staff', 'password', 'last_login', 'is_superuser', 'username')
        # Resto de tus opciones de configuración del formulario
        model = Trabajador
        fields = '__all__'
        labels = {
            'dni': 'DNI',
            'fecha_nacimiento': 'Fecha de Nacimiento',
            'direccion': 'Dirección',
            'telefono': 'Teléfono',
            'descripcion': 'Descripción',
        }
        widgets = {

            'direccion': forms.TextInput(attrs={'class': 'form-control'}),
            'telefono': forms.NumberInput(attrs={'class': 'form-control', 'type': 'number'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-select responsive-textarea', 'rows': 3, 'style': 'resize: none;'}),
        }
      

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        instance = kwargs.get('instance')
        if instance:
            self.fields['oficios'].widget.attrs.update({'class': 'form-control'})
            self.fields['dni'].disabled = True
            self.fields['dni'].widget.attrs['readonly'] = True


class ConsultaReclamoSugerenciaForm(forms.ModelForm):
    nombre = forms.CharField(max_length=100, label="Nombre", widget=forms.TextInput(attrs={'class': 'form-control'}))
    apellido = forms.CharField(max_length=100, label="Apellido", widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label="Email", widget=forms.EmailInput(attrs={'class': 'form-control'}))
    fecha_consulta = forms.DateField(required=False,label="Fecha de consulta", widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}))
    tipo = forms.ChoiceField(choices=TYPE_CHOICES, label="Tipo de contacto", widget=forms.Select(attrs={'class': 'form-control'}))
    mensaje = forms.CharField(label="Mensaje", widget=forms.Textarea(attrs={'class': 'form-control'}))
    class Meta:
        model = ConsultaReclamoSugerencia
        fields = ['nombre', 'apellido', 'email', 'fecha_consulta', 'tipo', 'mensaje']
            
    def clean_nombre(self):
        nombre = self.cleaned_data.get('nombre')
        if not nombre:
            raise forms.ValidationError("El Nombre es obligatorio.")
        return nombre

    def clean_apellido(self):
        apellido = self.cleaned_data.get('apellido')
        if not apellido:
            raise forms.ValidationError("El Apellido es obligatorio.")
        return apellido

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not email:
            raise forms.ValidationError("El Email es obligatorio.")
        return email

    def clean_fecha_consulta(self):
        fecha_consulta = self.cleaned_data.get('fecha_consulta')
        if fecha_consulta and fecha_consulta > timezone.now().date():
            raise forms.ValidationError("La fecha de consulta no puede ser mayor a la fecha actual.")
        return fecha_consulta
    
    def clean_mensaje(self):
        mensaje = self.cleaned_data.get('mensaje')
        if not mensaje:
            raise forms.ValidationError("El campo Mensaje es obligatorio.")
        return mensaje


class OficioForm(forms.ModelForm):
    def clean_nombre(self):
        # Validación del campo nombre
        data = self.cleaned_data["nombre"]
        # TODO: Validar que el oficio no este registrado en la base de datos
        if Oficio.objects.filter(nombre=data):
            raise ValidationError(
                'El oficio que esta ingresando, ya es esta registrado')
        return data

    class Meta:
        model = Oficio
        fields = '__all__'


class CustomUserCreationForm(UserCreationForm):
    first_name = forms.CharField(label="Nombre", max_length=30, required=True)
    last_name = forms.CharField(label="Apellido", max_length=30, required=True)
    photo = forms.ImageField(label="Foto", required=False)

    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields + ('first_name', 'last_name', 'photo',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance.pk:  # Si no hay instancia (usuario no registrado)
            self.fields['username'].disabled = True
            self.fields['username'].widget.attrs['readonly'] = True
            
class CustomUserModificationForm(forms.ModelForm):
    photo = forms.ImageField(label="Foto", required=True)
    class Meta:
        model = User
        fields = ['first_name', 'last_name','photo']
        
           
class AdminstracionTrabajadorForm(forms.ModelForm):
    email = forms.EmailField(label="Email", widget=forms.EmailInput(attrs={'class': 'form-control'}))
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['dni'].disabled = True
        self.fields['dni'].widget.attrs['readonly'] = True
    class Meta:
        model = Trabajador
        fields = '__all__'
        exclude = ('usuario', 'user_permissions', 'groups', 'is_active', 'date_joined',
                   'is_staff', 'password', 'last_login', 'is_superuser', 'username')
        widgets = {
            'fecha_nacimiento': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'dni': forms.NumberInput(attrs={'class': 'form-control'}),
            'direccion': forms.TextInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'telefono': forms.NumberInput(attrs={'class': 'form-control'}),
            'oficio': forms.Select(attrs={'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'foto': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }
    def clean_fecha_nacimiento(self):
        fecha_nacimiento = self.cleaned_data.get('fecha_nacimiento')
        if fecha_nacimiento:
            edad = timezone.now().date().year - fecha_nacimiento.year
            if edad < 18:
                raise ValidationError("Debes ser mayor de 18 años.")
        return fecha_nacimiento

    def clean_email(self):
        email = self.cleaned_data.get('email')

        # Obtener el valor original del campo email del objeto Trabajador
        original_email = self.instance.email

        # Verificar si el valor ha cambiado y ya existe otro Trabajador con el nuevo correo electrónico
        if email != original_email and Trabajador.objects.filter(email=email).exists():
            raise ValidationError("Este correo electrónico ya está registrado.")

        return email
