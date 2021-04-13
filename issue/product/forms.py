from .models import Category,Supplier

from django.forms import ModelForm,TextInput,Select,Textarea




class categoryForm(ModelForm):

    class Meta:
        model= Category
        fields = '__all__'

        labels = {

            'cat_name': 'Category Name',
            'parent_cat': 'Parent Category'
        }

        widgets = {
            'cat_name': TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Category Name','required':"true"}),
            'parent_cat': Select(attrs={'class': 'form-control',  'default': 'Select Parent Category Here...'})
        }

        

class supplierForm(ModelForm):

    class Meta:
        model= Supplier
        fields = '__all__'    

        widgets = {
            'supplier_address': Textarea(attrs={'rows':4}),
            'supplier_details': Textarea(attrs={'rows':4}),
           
        }        