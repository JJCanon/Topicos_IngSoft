from django import forms 
from django.core.exceptions import ValidationError
from django.shortcuts import render, redirect 
from django.views.generic import TemplateView
from django.views import View
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.
#Home view
class HomePageView(TemplateView):
    template_name = 'pages/home.html'
    
#About view
class AboutPageView(TemplateView): 
    template_name = 'pages/about.html' 
 
     
    def get_context_data(self, **kwargs): 
        context = super().get_context_data(**kwargs) 
        context.update({ 
            "title": "About us - Online Store", 
            "subtitle": "About us", 
            "description": "This is an about page ...", 
            "author": "Developed by: Your Name", 
        }) 
 
        return context 

#Contact view - First activity
class ContactPageView(TemplateView):
    template_name = 'pages/contact.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            "title": "Contact - Online Store",
            "email": "contact@onlinestore.com",
            "address": "123 Fake Street, Springfield",
            "phone": "+57 321 321 4321"
        })
        return context
    
    
class Product: 
    products = [ 
        {"id":"1", "name":"TV", "description":"Best TV","price":500}, 
        {"id":"2", "name":"iPhone", "description":"Best iPhone","price":300}, 
        {"id":"3", "name":"Chromecast", "description":"Best Chromecast","price":200}, 
        {"id":"4", "name":"Glasses", "description":"Best Glasses","price":100} 
    ] 
 
class ProductIndexView(View): 
    template_name = 'pages/products/index.html' 
 
    def get(self, request): 
        viewData = {} 
        viewData["title"] = "Products - Online Store" 
        viewData["subtitle"] =  "List of products" 
        viewData["products"] = Product.products 
 
        return render(request, self.template_name, viewData) 
 
#Actividad 4
class ProductShowView(View):
    template_name = 'pages/products/show.html'

    def get(self, request, id):
        viewData = {}

        # Verifica si el ID es válido
        try:
            product = Product.products[int(id) - 1]  # Intenta acceder al producto
        except (IndexError, ValueError):
            # Si el ID no es válido, redirige a la página de inicio
            return HttpResponseRedirect(reverse('home'))

        # Si el ID es válido, continúa con la lógica normal
        viewData["title"] = product["name"] + " - Online Store"
        viewData["subtitle"] = product["name"] + " - Product information"
        viewData["product"] = product

        return render(request, self.template_name, viewData)

#activity 7 
class ProductForm(forms.Form):
    name = forms.CharField(required=True)
    price = forms.FloatField(required=True)

    def clean_price(self):
        price = self.cleaned_data['price']
        if price <= 0:
            raise ValidationError("Price must be greater than zero.")
        return price

class ProductCreateView(View):
    template_name = 'pages/products/create.html'

    def get(self, request):
        form = ProductForm()
        viewData = {}
        viewData["title"] = "Create product"
        viewData["form"] = form
        return render(request, self.template_name, viewData)

    def post(self, request):
        form = ProductForm(request.POST)
        if form.is_valid():
            # Aquí podrías guardar el producto en la base de datos
            return render(request, 'products/success.html', {'title': 'Product Created'})
        else:
            viewData = {}
            viewData["title"] = "Create product"
            viewData["form"] = form
            return render(request, self.template_name, viewData)