from dataclasses import fields
from pyexpat import model
from django.forms import ModelForm, TextInput

from app.models import Product
from app.models import Transaction


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = "__all__"
        # widgets = {
        #     "email": EmailInput(attrs={
        #         "type": "email"
        #     })
        #   "no_calle": TextInput(attrs={
        #     "type": "number"
        #   })
        # }


class TransactionForm(ModelForm):
    class Meta:
        model = Transaction
        fields = "__all__"
