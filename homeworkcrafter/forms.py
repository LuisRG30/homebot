from django import forms 

grades = (
    ("Secundaria", "Secundaria"),
    ("Bachillerato", "Bachillerato"),
    ("Universidad", "Educación Superior")
)

subjects = (
    ("Matemáticas", "Matemáticas"),
    ("Español", "Lengua Española"),
    ("Física", "Física"),
    ("Química", "Química"),
    ("Programación", "Programación"),
    ("Ciencias Sociales", "Ciencias Sociales"),
    ("Negocios", "Administativas"),
    ("Otra", "Otra")
)

class RedeemForm(forms.Form):
    code = forms.CharField(label="Tu código", max_length=16)

class FeeForm(forms.Form):
    homework = forms.CharField(label="Tarea")
    name = forms.CharField(label="Nombre")
    email = forms.CharField(label="Correo Electrónico")
    number = forms.CharField(label="Teléfono")
    level = forms.CharField(label="Grado Académico", widget=forms.Select(choices=grades))
    subject = forms.CharField(label="Materia", widget=forms.Select(choices=subjects))
    date = forms.DateField(label="Fecha de Entrega", widget=forms.SelectDateWidget)
    file = forms.FileField(label="Adjunta un archivo", required=False)
    description = forms.CharField(widget=forms.Textarea, label="Descripción")

class MessageForm(forms.Form):
    name = forms.CharField()
    email = forms.CharField()
    message = forms.CharField(widget=forms.Textarea())