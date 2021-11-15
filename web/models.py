from django.db import models

# Create your models here.

class Product(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(blank=True, null=True)
    price = models.CharField(max_length=7)
    image = models.ImageField(upload_to='product')
    category = models.CharField(max_length=20)
    special = models.CharField(max_length=8, blank=True, null=True)

    def __str__(self):
        return f'(self.title)'


class Cart(models.Model):
    userID = models.TextField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()

    def sub_total(self):
        return self.product.price * self.quantity

    def __str__(self):
        return self.product

class Like(models.Model):
    userID = models.TextField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return self.product