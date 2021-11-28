# from django.db import models

# # Create your models here.

# class Product(models.Model):
#     title = models.CharField(max_length=100)
#     content = models.TextField(blank=True, null=True)
#     price = models.CharField(max_length=7)
#     image = models.ImageField(upload_to='product')
#     category = models.CharField(max_length=20)
#     special = models.CharField(max_length=8, blank=True, null=True)

#     def __str__(self):
#         return f'(self.title)'


# class Cart(models.Model):
#     userID = models.TextField()
#     product = models.ForeignKey(Product, on_delete=models.CASCADE)
#     quantity = models.IntegerField()

#     def sub_total(self):
#         return self.product.price * self.quantity

#     def __str__(self):
#         return self.product

# class Like(models.Model):
#     userID = models.TextField()
#     product = models.ForeignKey(Product, on_delete=models.CASCADE)

#     def __str__(self):
#         return self.product

from django.db import models


class Buy(models.Model):
    order = models.ForeignKey('OrderInfo', models.DO_NOTHING, db_column='order_ID', blank=True, null=True)  # Field name made lowercase.    
    product = models.ForeignKey('Product', models.DO_NOTHING, db_column='Product_ID', blank=True, null=True)  # Field name made lowercase.  

    class Meta:
        managed = False
        db_table = 'buy'


class Cart(models.Model):
    product = models.OneToOneField('Product', models.DO_NOTHING, db_column='product_ID', primary_key=True)  # Field name made lowercase.    
    user = models.ForeignKey('User', models.DO_NOTHING, db_column='user_ID')  # Field name made lowercase.
    quantity = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'cart'


class Coupon(models.Model):
    user = models.ForeignKey('User', models.DO_NOTHING, db_column='user_ID', blank=True, null=True)  # Field name made lowercase.
    coupon_num = models.IntegerField(db_column='coupon_Num', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'coupon'


class Event(models.Model):
    event_name = models.CharField(db_column='event_Name', primary_key=True, max_length=45)  # Field name made lowercase.
    user = models.ForeignKey('User', models.DO_NOTHING, db_column='user_ID')  # Field name made lowercase.
    participant_num = models.IntegerField(db_column='participant_Num', blank=True, null=True)  # Field name made lowercase.
    event_content = models.CharField(db_column='event_Content', max_length=500, blank=True, null=True)  # Field name made lowercase.        

    class Meta:
        managed = False
        db_table = 'event'


class Likes(models.Model):
    user = models.ForeignKey('User', models.DO_NOTHING, db_column='user_ID')  # Field name made lowercase.
    product = models.ForeignKey('Product', models.DO_NOTHING, db_column='Product_ID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'likes'


class OrderInfo(models.Model):
    order_id = models.IntegerField(db_column='order_ID', primary_key=True)  # Field name made lowercase.
    order_date = models.DateField(db_column='order_Date', blank=True, 
null=True)  # Field name made lowercase.
    total_price = models.IntegerField(db_column='total_Price', blank=True, null=True)  # Field name made lowercase.
    order_status = models.CharField(db_column='order_Status', max_length=45, blank=True, null=True)  # Field name made lowercase.
    user = models.ForeignKey('User', models.DO_NOTHING, db_column='user_ID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'order_info'


class Participate(models.Model):
    user = models.ForeignKey('User', models.DO_NOTHING, db_column='user_ID', blank=True, null=True)  # Field name made lowercase.
    event_name = models.ForeignKey(Event, models.DO_NOTHING, db_column='event_Name', blank=True, null=True)  # Field name made lowercase.   
    participation_date = models.DateField(db_column='participation_Date', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'participate'


class Product(models.Model):
    product_id = models.AutoField(db_column='product_ID', primary_key=True)  # Field name made lowercase.
    title = models.CharField(unique=True, max_length=45, blank=True, null=True)
    price = models.IntegerField(blank=True, null=True)
    image = models.CharField(unique=True, max_length=100, blank=True, 
null=True)
    category = models.CharField(max_length=45, blank=True, null=True) 
    detail_category = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product'


class Questionnaire(models.Model):
    q_id = models.CharField(db_column='q_ID', primary_key=True, max_length=45)  # Field name made lowercase.
    email = models.CharField(max_length=45, blank=True, null=True)    
    comment = models.CharField(max_length=500, blank=True, null=True) 
    user = models.ForeignKey('User', models.DO_NOTHING, db_column='user_ID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'questionnaire'


class Testtable(models.Model):
    is_success = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'testtable'


class User(models.Model):
    user_id = models.CharField(db_column='user_ID', primary_key=True, max_length=45)  # Field name made lowercase.
    password = models.CharField(max_length=45, blank=True, null=True) 
    user_name = models.CharField(db_column='user_Name', max_length=45, blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(unique=True, max_length=45, blank=True, null=True)
    point = models.IntegerField(blank=True, null=True)
    phone = models.CharField(db_column='Phone', max_length=45, blank=True, null=True)  # Field name made lowercase.
    city = models.CharField(max_length=45, blank=True, null=True)     
    gu = models.CharField(max_length=45, blank=True, null=True)       
    zipcode = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user'