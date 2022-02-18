from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# First model contains three attributes;
# User, name and email
class Customer(models.Model):
	user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
	name = models.CharField(max_length=200, null=True)
	email = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name


# This is the product model and contains "name", "price" and “digital” attributes.
# Digital will just be true or false and will let us know if this 
# is a digital product or a physical product that needs to be shipped
class Product(models.Model):
	name = models.CharField(max_length=200)
	price = models.FloatField()
	digital = models.BooleanField(default=False,null=True, blank=True)
    
    def __str__(self):
        return self.name

# The order Item model will be connected to
# the customer with a one to many relationship
# (AKA ForeignKey) and will hold the status of complete (True or False)
# and a transaction id along with the date this order was placed.
class Order(models.Model):
	customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)
	date_ordered = models.DateTimeField(auto_now_add=True)
	complete = models.BooleanField(default=False)
	transaction_id = models.CharField(max_length=100, null=True)

	def __str__(self):
		return str(self.id)

# This model will need a product attribute connected
# to the product model, the order this item is connected to,
# quantity and the date this item was added to cart.
class OrderItem(models.Model):
	product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
	order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
	quantity = models.IntegerField(default=0, null=True, blank=True)
	date_added = models.DateTimeField(auto_now_add=True)

# This model will be a child to order and 
# will only be created if at least one orderitem
# within an order is a physical product (If Product.digital == False).
class ShippingAddress(models.Model):
	customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)
	order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
	address = models.CharField(max_length=200, null=False)
	city = models.CharField(max_length=200, null=False)
	state = models.CharField(max_length=200, null=False)
	zipcode = models.CharField(max_length=200, null=False)
	date_added = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.address