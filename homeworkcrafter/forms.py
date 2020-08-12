from django import forms 

class RedeemForm(forms.Form):
    code = forms.CharField(label="Tu código", max_length=16)

class FeeForm(forms.Form):
    homework = forms.CharField(label="Tarea*")
    email = forms.EmailField(label="Correo Electrónico*")
    number = forms.CharField(label="Teléfono*")
    subject = forms.CharField(label="Materia*")
    date = forms.DateField(label="Fecha de Entrega*")
    instructions_file = forms.FileField(label="Adjunta un archivo")
    description = forms.Textarea(label="Descripción")

