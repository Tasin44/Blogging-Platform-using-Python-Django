from django.urls import path
from . import views


urlpatterns = [
    # path('home', views.home, name='home'),
    path('', views.product_list, name='product_list'),
    path('<int:pk>/', views.product_detail, name='product_detail'),
    path('<int:pk>/edit/', views.edit_product, name='edit_product'),
    path('<int:pk>/delete/', views.delete_product, name='delete_product'),
]

'''
1.path('', views.product_list, name='product_list'):
The root URL (/) maps to product_list, displaying all products.

2.path('<int:pk>/', views.product_detail, name='product_detail'):
(i)Dynamic URL that accepts an integer (pk) and calls the product_detail view to show the details of a specific product.

(ii)Maps URLs like /1/, where 1 is a product's primary key, to product_detail, showing details for that specific product.

3.path('<int:pk>/edit/', views.edit_product, name='edit_product'):
(i)URL that allows editing of a specific product by its primary key.
(ii)Maps URLs like /1/edit/ to edit_product, allowing users to edit a specific product.

4.path('<int:pk>/delete/', views.delete_product, name='delete_product'):
(i)URL for deleting a specific product by its primary key.
(ii)Maps URLs like /1/delete/ to delete_product, enabling users to delete a specific product.


'''