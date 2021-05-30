from django.db import models

# Create your models here.

class Product(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    price = models.CharField(max_length=7) #최대 999,999
    image = models.ImageField(upload_to='product')

    def __str__(self):
        return f'(self.title)'

#migration 아직 안함