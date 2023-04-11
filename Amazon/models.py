from django.db import models
from django.shortcuts import reverse


# Create your models here. --> python class

class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.name



class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField(default=0)
    description = models.CharField(max_length=200, null=True, blank=True)
    instock = models.BooleanField(null=True)
    image = models.ImageField(upload_to='products/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at =  models.DateTimeField(auto_now=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE,
                                 null=True, blank=True, related_name='catproducts')


    def __str__(self):
        return self.name


    def get_image_url(self):
        return f"/media/{self.image}"


    def get_show_url(self):
        url = reverse('db.products.show', args=[self.id])
        return url

    def get_delete_url(self):
        url = reverse('db.products.delete', args=[self.id])
        return url

    def get_edit_url(self):
        url = reverse('db.products.edit', args=[self.id])
        return url


    @classmethod
    def get_product(cls, id):
        return Product.objects.get(id=id)


    def delete_product(self):
        return  self.delete()