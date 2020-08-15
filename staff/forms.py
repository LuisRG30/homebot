from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Username', 'class': 'input100'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password', 'class': 'input100'}))

class SearchForm(forms.Form):
    pass

class DeliveryForm(forms.Form):
    file = forms.FileField(label="Adjunta un archivo", required=False)