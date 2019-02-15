from django import forms

class TransactionForm(forms.Form):
    withdrawal = forms.DecimalField(max_digits=5, decimal_places=2)
    deposit = forms.DecimalField(max_digits=20, decimal_places=2)
    