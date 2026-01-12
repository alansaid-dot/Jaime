from django import forms

class NewDepartamentoForm(forms.Form):
    departamento = forms.CharField(max_length=50)
    shorname = forms.CharField(max_length=20)