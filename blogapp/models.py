from django.db import models
#This file defines your data structure by creating models that represent 
# your database tables.

# Here we have created a Product table with name, description, 
# image, created_at, and updated_at fields in the table.

from django.db import models

class Product(models.Model):
    name=models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='products/')
    #upload_to='products/' option specifies the folder inside the media directory where product images will be stored.
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):#Returns the string representation of the object (the product's name).
        return self.name
    
    def edit(self,name,description,image):
        self.name=name
        self.description=description
        self.image=image
        self.save()
    
    def short_description(self): # returns a shortened version of the product description (up to 30 words)
        words = self.description.split()
        if len(words)>50:
            return ' '.join(words[:30]) + '...'
        else:
            return self.description

'''
short_description():
This method truncates the product description to the first 30 words 
if it exceeds 50 words, appending '...' to indicate there is more content.

Key Components
1.
.split():
(i)The .split() method is a string method in Python that divides a string into 
a list of words based on whitespace (spaces, tabs, newlines).

(ii)In this context, self.description.split() takes the product description 
and creates a list of words. 

For example, if the description is "This is a sample product description.", 
it would return ['This', 'is', 'a', 'sample', 'product', 'description.'].

2.
.join():
(i)The .join() method is used to concatenate elements of an iterable 
(like a list) into a single string, with a specified separator.
(ii)In this case, ' '.join(words[:30]) joins the first 30 words from the list created by .split(), using a space as the separator. 
This means if there are more than 50 words in the description, only the first 30 will be included in the returned string.

words[]:
The words[:30] syntax slices the list of words to get only the first 30 elements. 
If there are more than 50 words in total, this ensures that only a limited number of words are included in the shortened description.

'''








