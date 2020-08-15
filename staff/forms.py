from django import forms

class LoginForm(forms.Form):
    pass

class SearchForm(forms.Form):
    pass

class DeliveryForm(forms.Form):
    file = forms.FileField(label="Adjunta un archivo", required=False)