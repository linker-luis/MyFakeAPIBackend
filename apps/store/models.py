from django.db import models
from apps.fakeuser.models import FakeUser

class Category(models.Model):
    name = models.CharField(max_length= 40)
    description = models.TextField()

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length= 100, blank= True, null = True)
    category = models.ForeignKey(Category, on_delete= models.SET_NULL, null= True, related_name= 'category')
    price = models.DecimalField(max_digits= 6, decimal_places= 2, null= True, blank= True)
    description = models.TextField(null= True, blank= True)

    def __str__(self):
        return self.name

class Images(models.Model):
    product = models.ForeignKey(Product, on_delete= models.CASCADE, related_name= 'images')
    # img = models.ImageField(upload_to = 'store/', null = True)
    imgURL = models.URLField(max_length= 255)

    def __str__(self):
        return f'{self.id}-{self.product.name}'

class Details(models.Model):
    detail = models.TextField(null= True, blank= True)
    product = models.ForeignKey(Product, on_delete= models.CASCADE, related_name= 'details')

    def __str__(self):
        return f'{self.id} {self.product.name}'


##### cart #######

class Cart(models.Model):
    user = models.ForeignKey(FakeUser, on_delete= models.CASCADE)

    # @property  --> al parecer properti tambien se encarga de parsear los valore resultante en una funcion dentro de un modelos a int o str 
    def get_total_price(self):
        products = self.products.all()
        # print(products[0].get_total)
        total_price = sum([product.get_total for product in products])
        # total_price = True
        return total_price

    @property
    def get_total_quantity(self):
        products = self.products.all()
        total_quantity = sum([product.quantity for product in products])
        return total_quantity

    def __str__(self):
        return f'{self.user.username}'


class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete= models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete= models.CASCADE, related_name= 'products')
    quantity = models.IntegerField(default= 0, null= True, blank= True)

    @property
    def get_total(self):
        total = self.product.price * self.quantity
        return total

    def __str__(self):
        return self.product.name