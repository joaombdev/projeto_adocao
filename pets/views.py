from django.shortcuts import render, redirect
from pets.models import Pet
from pets.forms import PetModelForm
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
# Create your views here.

class NewPetCreateView(CreateView):
    model = Pet
    form_class = PetModelForm
    template_name = 'new_pet.html'
    success_url = '/pets/'

class PetListView(ListView):
    model = Pet
    template_name = 'pets.html'
    context_object_name = 'pets'

class PetDetailView(DetailView):
    model = Pet
    template_name = 'pet_detail.html'

class PetUptadeView(UpdateView):
    model = Pet 
    form_class = PetModelForm
    template_name = 'car_update.html'
    success_url = '/pets/'

class PetDeleteView(DeleteView):
    model = Pet
    template_name = 'car_delete.html'
    success_url = '/pets/'

