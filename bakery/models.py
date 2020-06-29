from django.db import models

# Create your models here.
class category(models.Model):
	name=models.CharField(max_length=200)
	class Meta:
		db_table="category"
	def __str__(self):
		return self.name

class products(models.Model):
	name=models.CharField(max_length=200)
	category=models.ForeignKey(category,on_delete=models.CASCADE,related_name='products')
	pick=models.ImageField(upload_to = 'image/')
	price=models.CharField(max_length=200)
	class Meta:
		db_table="products"
	def __str__(self):
		return self.name
		
class contact(models.Model):
	name=models.CharField(max_length=200)
	phone=models.CharField(max_length=200)
	email=models.CharField(max_length=200)
	message=models.CharField(max_length=200)
	class Meta:
		db_table="contact"
	def __str__(self):
		return self.name
		
		
class order(models.Model):
	name=models.CharField(max_length=200)
	phone=models.CharField(max_length=200)
	product=models.CharField(max_length=200)
	email=models.CharField(max_length=200)
	address=models.CharField(max_length=200)
	class Meta:
		db_table="order"
	def __str__(self):
		return self.name