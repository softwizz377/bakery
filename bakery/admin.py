from django.contrib import admin
from bakery.models import category,products, contact, order
# Register your models here.

@admin.register(category)
class categoryadmin(admin.ModelAdmin): 
	pass

@admin.register(products)
class productadmin(admin.ModelAdmin):
	pass
    
@admin.register(contact)
class contactadmin(admin.ModelAdmin):
	list_display=('name','phone','email','message',)

@admin.register(order)
class orderadmin(admin.ModelAdmin):
	list_display=('name','phone','product','email','address',)

