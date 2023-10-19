from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import SuperHero

# custom imports
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, UpdateView
from .forms import SuperHeroForm


class MyLoginView(LoginView):
    template_name = 'registration/login.html'
    success_url = reverse_lazy('legal:list')


class SuperHeroCreateView(CreateView):
    model = SuperHero
    form_class = SuperHeroForm
    template_name = 'assessment/superhero_form.html'
    success_url = reverse_lazy('legal:list')


class SuperHeroUpdateView(UpdateView):
    model = SuperHero
    form_class = SuperHeroForm
    template_name = 'assessment/superhero_form.html'
    success_url = reverse_lazy('legal:list')


class SuperHeroListView(LoginRequiredMixin, ListView):
    model = SuperHero
    login_url = reverse_lazy('legal:login')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class SuperHeroDetailView(LoginRequiredMixin, DetailView):
    model = SuperHero
    login_url = reverse_lazy('legal:login')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print(context)
        return context
