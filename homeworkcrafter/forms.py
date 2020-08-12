from django import forms 

class RedeemForm(forms.Form):
    code = forms.CharField(label="Tu código", max_length=16)

