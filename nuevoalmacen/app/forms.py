from dataclasses import fields
from django.forms import ModelForm, TextInput

from app.models import Product


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
