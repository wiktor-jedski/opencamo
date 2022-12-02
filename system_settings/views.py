from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.shortcuts import render
from django.urls import reverse
from django.views import generic

from system_settings.models import Unit, Airport, Location


class CreateUnit(LoginRequiredMixin, generic.CreateView):
    fields = ('name', 'unit')
    model = Unit

    def get_success_url(self):
        return reverse('system_settings:unit_add')

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            messages.success(request, "Unit successfully added.")
        response = super().post(request, *args, **kwargs)
        return response


class CreateAirport(LoginRequiredMixin, generic.CreateView):
    fields = ('IATA_code', 'name', 'alias', 'address')
    model = Airport

    def get_success_url(self):
        return reverse('system_settings:airport_add')

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            messages.success(request, "Airport successfully added.")
        response = super().post(request, *args, **kwargs)
        return response


class CreateLocation(LoginRequiredMixin, generic.CreateView):
    fields = ('name', 'alias', 'address')
    model = Location

    def get_success_url(self):
        return reverse('system_settings:location_add')

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            messages.success(request, "Location successfully added.")
        response = super().post(request, *args, **kwargs)
        return response


class ListLocation(LoginRequiredMixin, generic.ListView):
    model = Location
