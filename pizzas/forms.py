from django import forms
from .models import Order,Sales



class PizzaForm(forms.ModelForm):
    
    class Meta:
        model = Order
        fields = (
            'size',
            'quantity',
        )
        widgets = {
            'size':forms.RadioSelect,
            'quantity': forms.TextInput(attrs={'class' : "rounded border border-warning form-control", "style" : "width: 50%;"}),          
        }
class SalesForm(forms.ModelForm):
    class Meta:
        model=Sales
        fields = (
        'name',
        'surname',
         'phone',
         'address',
        )
        widgets = {
         
          'name': forms.TextInput(attrs={'class' : "rounded text-center border border-warning form-control", "style" : "width: 50%"}),
           'surname': forms.TextInput(attrs={'class' : "rounded   text-center border border-warning form-control", "style" : 
 "width: 50%;"}),          
   'phone': forms.TextInput(attrs={'class' : "rounded text-center border border-warning form-control", "style" : 
 "width: 50%;"}),          
   'address': forms.TextInput(attrs={'class' : "rounded text-center border border-warning form-control", "style" : 
 "width: 50%;"}),                    
         }       