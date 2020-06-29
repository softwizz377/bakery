from django.shortcuts import render,redirect
from django.views.generic import TemplateView
from bakery.models import category, contact,order
from bakery.models import products
from bakery.forms import contactform
from bakery.forms import orderform
from cart.forms import CartAddProductForm

# Create your views here.
class bakery1pageview(TemplateView):
	template_name="bakery1.html"
	
class menupageview(TemplateView):
	template_name="menu.html"	
class aboutpageview(TemplateView):
	template_name="about.html"	
'''class productspageview(TemplateView):
	template_name="products.html"'''	
class servicespageview(TemplateView):
	template_name="services.html"
class offerpageview(TemplateView):
	template_name="offer.html"	
class blogpageview(TemplateView):
	template_name="blog.html"	
class contactspageview(TemplateView):
	template_name="contacts.html"
'''class orderpageview(TemplateView):
	template_name="order.html"'''
		

def insertcontact(request):
	if request.method=='POST':
		form=contactform(request.POST)
		if form.is_valid():
			try:
				form.save()
				return redirect('/contacts/')
			except:
				pass
	
	else:
		form=contactform()
		
	return render(request,'contacts.html',{'form':form})	


def insertorder(request):
	if request.method=='POST':
		form=orderform(request.POST)
		if form.is_valid():
			try:
				form.save()
				return redirect('/order/')
			except:
				pass
	
	else:
		form=orderform()
		
	return render(request,'order.html',{'form':form})		
    
def product_list(request):
   category_list = category.objects.all()
   cart_product_form = CartAddProductForm()
   context = {
        'cat': category_list,
        'cart_product_form': cart_product_form
    }
   return render(request, 'products.html', context)    

def productlist(request):
    product_list = products.objects.all()
    context_dict={'pro':product_list,}
    return render(request, 'order.html', context_dict)    