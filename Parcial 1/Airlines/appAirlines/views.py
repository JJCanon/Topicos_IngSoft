from django.shortcuts import render
from django.views.generic import TemplateView, CreateView
from .models import Airline
from .forms import AirlineForm
from django.urls import reverse_lazy
# Create your views here.

#Home view
class Home(TemplateView):
    template_name = 'Airlines/home.html'
    
# Create Flight view
class CreateFlight(CreateView):
    model = Airline
    form_class = AirlineForm
    template_name = 'Airlines/createFlight.html'
    success_url = reverse_lazy('home')
    
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

# List of flights view
class ListFlights(TemplateView):
    template_name = 'Airlines/listFlights.html'
    
    #listar vuelos orden por precio
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['flights'] = Airline.objects.all().order_by('price')
        return context

    
    