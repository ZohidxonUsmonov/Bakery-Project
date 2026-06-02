from django.db import models

# Create your models here.

class Service(models.Model):
    title=models.CharField(max_length=200)
    description=models.TextField()
    image=models.ImageField(upload_to='services/')
    link=models.URLField(max_length=200,blank=True,null=True)

    def __str__(self):
        return self.title

class Category(models.Model):
    name=models.CharField(max_length=200)
    slug=models.SlugField(unique=True)
    def __str__(self):
        return self.name

class Product(models.Model):
    category=models.ForeignKey(Category,on_delete=models.CASCADE,related_name='products',null=True,blank=True)
    title=models.CharField(max_length=200)
    price=models.DecimalField(max_digits=10,decimal_places=2)
    image=models.ImageField(upload_to='products/')


    def __str__(self):
        return self.title


