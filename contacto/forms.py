from django import forms

class formularioContacto(forms.Form):
    nombre = forms.CharField(label="Nombre", required=True)
    correo = forms.EmailField(label="Correo", required=True)
    contenido = forms.CharField(
        label="Contenido",
        widget=forms.Textarea,
        required=True
    )
