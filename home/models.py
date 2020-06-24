from django.db import models

class Contact(models.Model):
    name=models.CharField( max_length=100)
    email=models.EmailField( max_length=254)
    phone=models.CharField(max_length=10)
    desc=models.TextField()
    date=models.DateField()

    def __str__(self):
        return self.name 

class ProductView(models.Model):
    
    pname=models.CharField( max_length=300)
    pcategory=models.CharField( max_length=300)
    psubcategory=models.CharField( max_length=300)
    pdesc=models.CharField( max_length=1000)
    pprice=models.IntegerField()
    pdate=models.DateField()
    
    

    def __str__(self):
        return self.pname
    

    

# Create your models here.
