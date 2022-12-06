from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse
from django.views import generic

from engineering.models import ACModel, AC, Effectivity, Control, RotablePN, RepairablePN, ExpendablePN


class GeneralCreateView(LoginRequiredMixin, generic.CreateView):
    reverse_to = 'reverse_link'
    success_message = 'success_message'

    def get_success_url(self):
        return reverse(self.reverse_to)

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            messages.success(request, self.success_message)
        response = super(GeneralCreateView, self).post(request, *args, **kwargs)
        return response


class CreateACModel(GeneralCreateView):
    fields = ('ac_model_name',)
    model = ACModel
    reverse_to = 'engineering:ac_model_add'
    success_message = 'Aircraft model added.'


class CreateAC(GeneralCreateView):
    fields = ('call_sign', 'line_number', 'ac_model')
    model = AC
    reverse_to = 'engineering:ac_add'
    success_message = 'Aircraft added.'


class CreateEffectivity(GeneralCreateView):
    reverse_to = 'engineering:effectivity_add'
    success_message = 'Effectivity added.'
    fields = '__all__'
    model = Effectivity


class CreateControl(GeneralCreateView):
    reverse_to = 'engineering:control_add'
    success_message = 'Controls added.'
    fields = ('control_name', 'interval_type', 'interval_day_count', 'interval_cycle_count')
    model = Control


class CreateRotablePN(GeneralCreateView):
    reverse_to = 'engineering:rotable_pn_add'
    success_message = 'PN added.'
    fields = '__all__'
    model = RotablePN


class CreateRepairablePN(GeneralCreateView):
    reverse_to = 'engineering:repairable_pn_add'
    success_message = 'PN added.'
    fields = '__all__'
    model = RepairablePN


class CreateExpendablePN(GeneralCreateView):
    reverse_to = 'engineering:expendable_pn_add'
    success_message = 'PN added.'
    fields = '__all__'
    model = ExpendablePN
