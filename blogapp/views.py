from django.http import HttpResponse
from django.shortcuts import render
from .models import Product
from django.shortcuts import render,redirect,get_object_or_404
from .models import Product #Importing the Model from models.py
from .forms import ProductForm #Importing the ProductForm from the forms.py


# Create your views here.
def product_list(request):
    products = Product.objects.all()
    return render(request, 'index.html', {'products': products})

def product_detail(request, pk):
    product = Product.objects.get(pk=pk)
    return render(request, 'index2.html', {'product': product})


def edit_product(request, pk):#has relation with forms.py ProductForm class
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm(instance=product)
    return render(request, 'edit.html', {'form': form})

def delete_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        product.delete()
        return redirect('product_list')
    return render(request, 'delete.html', {'product': product})

# def home(request):
#     return HttpResponse('Hello, World!')

'''
1. views.py
This file contains your views, which handle the logic of what data to show and which template to render for different requests.

1.1. product_list(request):
(i)Retrieves all products from the database using Product.objects.all().
(ii)Renders the index.html template, passing the list of products as context.
The render() function takes three arguments: 
the HTTP request, the template to render (index.html), 
and a context dictionary where 'products': products passes the list of products to the template.

1.2. product_detail(request, pk):

(i)Product.objects.get(pk=pk): Fetches a specific product from database using its primary key (pk)
Renders the index2.html template, passing the product details as context.


1.3. edit_product(request, pk):handles editing a product by its pk;
(i)get_object_or_404(Product, pk=pk) either fetches the product with the given pk, or returns a 404 error if it doesn’t exist.

(ii)If the request method is POST, the form data is submitted.
If the form is valid, it saves the updated product and redirects to the product list.

(iii)If the request method is GET, it initializes the form with the existing product data.

(iv)Renders the edit.html template with the form for editing.


1.4. delete_product(request, pk):
(i)Like the edit view, get_object_or_404() retrieves the product or raises a 404 error.
(ii)If the request method is POST, it deletes the product and redirects to the product list.
(iii)If GET, it renders a confirmation page (delete.html) for deletion.


'''