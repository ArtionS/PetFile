# from django.shortcuts import render

from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse

# Paquete para pedir que se este en modo login
from django.contrib.auth.mixins import LoginRequiredMixin

# Modelos de Proceso
from .models import Vaccine, Pet


class VaccineList(LoginRequiredMixin, ListView):
    model = Vaccine
    context_object_name = 'vaccines'
    template_name = 'vaccine/vaccine_list.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        newPet = Pet()
        newPet.id = self.kwargs['id_pet']
        context['vaccines'] = context['vaccines'].filter(pet_id=newPet.id)
        context['id_pet'] = self.kwargs['id_pet']
        return context


class VaccineDetail(LoginRequiredMixin, DetailView):
    model = Vaccine
    context_object_name = 'vaccines'
    template_name = 'vaccine/vaccine_detail.html'
    pk_url_kwarg = "id_vac"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['id_pet'] = self.kwargs['id_pet']
        return context


class VaccineCreate(LoginRequiredMixin, CreateView):
    model = Vaccine
    fields = [
        'name',
    ]
    template_name = 'vaccine/vaccine_form.html'

    def get_success_url(self):
        return reverse('vaccine_list' , kwargs=self.kwargs)

    def form_valid(self, form):
        newpet = Pet()
        newpet.id = self.kwargs['id_pet']
        form.instance.pet_id = newpet
        return super(VaccineCreate, self).form_valid(form)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = {
            'id_pet' : self.kwargs['id_pet'],
            'form': self.get_form()
        }
        return context


class VaccineUpdate(LoginRequiredMixin, UpdateView):
    model = Vaccine
    fields = [
        'name',
    ]
    pk_url_kwarg = "id_pro"

    def get_success_url(self):
        return reverse('vaccine_detail' , kwargs=self.kwargs)

    def form_valid(self, form):
        newpet = Pet()
        newpet.id = self.kwargs['id_pet']
        form.instance.pet_id = newpet
        return super(VaccineUpdate, self).form_valid(form)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = {
            'id_pet' : self.kwargs['id_pet'],
            'form': self.get_form()
        }
        return context


class VaccineDelete(LoginRequiredMixin, DeleteView):
    model = Vaccine
    template_name = 'vaccine/vaccine_confirm_delete.html'
    context_object_name = 'vaccines'
    pk_url_kwarg = "id_vac"

    def get_success_url(self):
        context = {
            'id_pet' : self.kwargs['id_pet']
        }
        return reverse('vaccine_list' , kwargs=context)

    def form_valid(self, form):
        return super(VaccineDelete, self).form_valid(form)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = {
            'id_pet' : self.kwargs['id_pet'],
            'id_vac': self.kwargs['id_vac'],
            'form': self.get_form(),
            'obj' : self.object
        }
        return context
