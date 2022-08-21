# from django.shortcuts import render

from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse

# Paquete para pedir que se este en modo login
from django.contrib.auth.mixins import LoginRequiredMixin

# Modelos de Proceso
from .models import Process, Pet


class ProcessList(LoginRequiredMixin, ListView):
    model = Process
    context_object_name = 'pros'
    template_name = 'process/process_list.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        # print(kwargs)
        # print("test 1")
        # print(self.kwargs['id_pet'])

        context = super().get_context_data(**kwargs)
        # print("test 2")
        # print(context)
        #
        # print("test 2.1")
        # print(context['pros'][1].pet_id)
        # print("test 2.2")
        # print(self.kwargs['id_pet'])
        #
        # print("test 2.3 request")
        # print(self.request.user)

        newPet = Pet()
        newPet.id = self.kwargs['id_pet']
        context['pros'] = context['pros'].filter(pet_id=newPet.id)
        context['id_pet'] = self.kwargs['id_pet']

        return context



class ProcessDetail(LoginRequiredMixin, DetailView):
    model = Process
    context_object_name = 'pro'
    template_name = 'process/process_detail.html'
    pk_url_kwarg = "id_pro"

    def get_context_data(self, *, object_list=None, **kwargs):
        # print("HardCode")
        # print(kwargs)
        context = super().get_context_data(**kwargs)
        context['id_pet'] = self.kwargs['id_pet']
        # context['pets'] = context['pets'].filter(id_pet=self.request.id_pet)

        return context


class ProcessCreate(LoginRequiredMixin, CreateView):
    model = Process
    # fields = '__all__'
    fields = [
        'type_process',
        'title',
        'description',
        'weight',
    ]
    template_name = 'process/process_form.html'
    # context_object_name = 'prosss'
    # success_url = reverse('process_list')

    def get_success_url(self):
        # print(self)
        # print("hardcoding")
        # print(self.kwargs['id_pet'])
        return reverse('process_list' , kwargs=self.kwargs)


    def form_valid(self, form):
        print("Holitas")
        print(form.instance.pet_id)

        newpet = Pet()
        newpet.id = self.kwargs['id_pet']

        form.instance.pet_id = newpet
        return super(ProcessCreate, self).form_valid(form)

    def get_context_data(self, *, object_list=None, **kwargs):

        print(self.kwargs['id_pet'])

        # self.kwargs['id_pet'] = self.kwargs['id_pet'],
        #
        # super(ProcessCreate, self).get_context_data()
        context = {
            'id_pet' : self.kwargs['id_pet'],
            'form': self.get_form()
        }
        # super(ProcessCreate, self).get_context_data()
        # super(ProcessCreate, self).get_context_data(kwargs=context)
        return context


class ProcessUpdate(LoginRequiredMixin, UpdateView):
    model = Process
    fields = [
        'type_process',
        'title',
        'description',
        'weight',
    ]
    pk_url_kwarg = "id_pro"


    def get_success_url(self):
        # print(self)
        # print("HardCoding Update Success")
        # print(self.kwargs['id_pet'])
        return reverse('process_detail' , kwargs=self.kwargs)

    def form_valid(self, form):
        newpet = Pet()
        newpet.id = self.kwargs['id_pet']
        form.instance.pet_id = newpet
        return super(ProcessUpdate, self).form_valid(form)

    def get_context_data(self, *, object_list=None, **kwargs):

        print(self.kwargs['id_pet'])

        # self.kwargs['id_pet'] = self.kwargs['id_pet'],
        #
        # super(ProcessCreate, self).get_context_data()
        context = {
            'id_pet' : self.kwargs['id_pet'],
            'form': self.get_form()
        }
        # super(ProcessCreate, self).get_context_data()
        # super(ProcessCreate, self).get_context_data(kwargs=context)
        return context


class ProcessDelete(LoginRequiredMixin, DeleteView):
    model = Process
    template_name = 'process/process_confirm_delete.html'
    context_object_name = 'pro'
    pk_url_kwarg = "id_pro"

    def get_success_url(self):
        context = {
            'id_pet' : self.kwargs['id_pet']
        }
        return reverse('process_list' , kwargs=context)

    def form_valid(self, form):
        return super(ProcessDelete, self).form_valid(form)

    def get_context_data(self, *, object_list=None, **kwargs):
        # print(self.__dict__)
        # print("HardCoding Update Get Context DELETE")
        # print(self.kwargs)
        # print(self.kwargs['id_pet'])
        # print(self.object)

        context = {
            'id_pet' : self.kwargs['id_pet'],
            'id_pro': self.kwargs['id_pro'],
            'form': self.get_form(),
            'obj' : self.object
        }

        print(context)

        return context
