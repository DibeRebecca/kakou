from django.db import models

# Create your models here.
"""ARTICLES={
    'chaussures':{'name':'gucci'},
    'habits':{'name':'lacoste'},
    'jupes':{'name':'taille-haute'},
    'chaines':{'name':'pendentif'},
}
CATEGORIE=[
    {'name':'yan','articles':[ARTICLES['chaussures']]},
    {'name':'rebecca','articles':[ARTICLES['habits']]},
    {'name':'arthur','articles':[ARTICLES['jupes']]},
    {'name':'loas','articles':[ARTICLES['chaines']]},
]"""

class Categories(models.Model):
    name= models.CharField(max_length=300)
    
    def __str__(self):
        return self.name

class Articles(models.Model):
    name= models.CharField(max_length=300)
    price=models.IntegerField()
    quantity=models.IntegerField()
    available=models.BooleanField(default=True)
    picture=models.ImageField()
    created_at=models.DateTimeField(auto_now_add=True)
    categorie=models.ForeignKey(Categories,on_delete=models.CASCADE)  

    def __str__(self):
        return self.name



class Contact(models.Model):
    name=models.EmailField(max_length=200,unique=True)
    email=models.CharField(max_length=100,unique=True)

    def __str__(self):
        return self.name

class Reservation(models.Model):
    created_at=models.DateTimeField(auto_now_add=True)
    contacted=models.BooleanField(default=True)
    contact=models.ForeignKey(Contact,on_delete=models.CASCADE)
    article=models.OneToOneField(Articles,on_delete=models.CASCADE)

    def __str__(self):
        return self.contact




