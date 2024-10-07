#forms.py responsible for defining forms that facilitate user input and data validation.


from django import forms
#This imports Django's forms module, which provides various classes and methods to create and handle forms easily.
from .models import Product

class ProductForm(forms.ModelForm):
    
    class Meta:
        model = Product
        fields = ['name','description','image']

'''
class ProductForm(forms.ModelForm): relation with (class Product of models.py) 

This line defines a new class called ProductForm,which inherits from forms.ModelForm. 

A ModelForm is a special type of form in Django that automatically 
generates form fields based on a specified model. 

This form is used to handle input and validation of data related to a Product object, 
which includes fields like name, description, and image.


Meta class: 
The inner Meta class specifies that this form is associated with the 
Product model(class Product of models.py) and includes the fields name, description, and image.

(i)Meta: This is an inner class in Django that provides metadata about the form.

(ii)model = Product: means (class Product of models.py)
Form should be associated with the Product model.Any form submission will be linked to this model, 
allowing us to create or edit Product instances using the form


(iii)fields = ['name', 'description', 'image']: 
It has a relation with def edit(self,name,description,image) of models.py

This specifies which fields from the Product model should be included in the form. 
In this case, the form will have input fields for:

name: Text input (CharField)
description: Text area (TextField)
image: File input (ImageField)

'''