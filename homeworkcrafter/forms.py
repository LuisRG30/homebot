from django import forms 

grades = (
    ("secundaria", "secundaria"),
    ("bachillerato", "bachillerato"),
    ("universidad", "Educación Superior")
)

subjects = (
    ("mate", "Matemáticas"),
    ("esp", "Lengua Española"),
    ("physics", "Física"),
    ("chemistry", "Química"),
    ("coding", "Programación"),
    ("social", "Ciencias Sociales"),
    ("bussiness", "Administativas"),
    ("other", "Otro")
)

class RedeemForm(forms.Form):
    code = forms.CharField(label="Tu código", max_length=16)

class FeeForm(forms.Form):
    homework = forms.CharField(label="Tarea")
    email = forms.EmailField(label="Correo Electrónico")
    number = forms.CharField(label="Teléfono")
    level = forms.CharField(label="Grado Académico", widget=forms.Select(choices=grades))
    subject = forms.CharField(label="Materia", widget=forms.Select(choices=subjects))
    date = forms.DateField(label="Fecha de Entrega", widget=forms.SelectDateWidget)
    instruction_file = forms.FileField(label="Adjunta un archivo", required=False)
    description = forms.CharField(widget=forms.Textarea, label="Descripción")

