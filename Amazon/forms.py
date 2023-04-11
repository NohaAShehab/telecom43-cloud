
from django import forms
from Amazon.models import  Product


### python --> create form ---> according to the model

class ProductModelForm(forms.ModelForm):
    class Meta:
        model= Product
        fields='__all__'

