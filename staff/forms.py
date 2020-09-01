from django import forms

grades = (
    (1, 1),
    (2, 2),
    (3, 3),
    (4, 4),
    (5, 5)
)

class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Username', 'class': 'input100'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password', 'class': 'input100'}))

class SearchForm(forms.Form):
    pass

class DeliveryForm(forms.Form):
    file = forms.FileField(label="Adjunta un archivo", required=False)

class ReviewForm(forms.Form):
    code = forms.CharField(label="Código de tu pedido")
    rating = forms.IntegerField(widget=forms.Select(choices=grades), label="Calificación")
    comment = forms.CharField(widget=forms.Textarea, label="Comentario")

class PriceForm(forms.Form):
    price = forms.IntegerField(label="Precio", widget=forms.NumberInput(attrs={'class': 'input100'}))