from django.db import models
from django.utils.translation import gettext_lazy as _

from system_settings.models import Unit


class ACModel(models.Model):
    ac_model_name = models.CharField(max_length=10)

    def __str__(self):
        return self.ac_model_name


class AC(models.Model):
    call_sign = models.CharField(max_length=10, unique=True)
    line_number = models.IntegerField(blank=True, null=True)
    ac_model = models.ForeignKey(ACModel, on_delete=models.CASCADE)

    def __str__(self):
        return self.call_sign


class Effectivity(models.Model):
    effectivity_name = models.CharField(max_length=100, unique=True)
    ac = models.ManyToManyField(AC)

    def __str__(self):
        return self.effectivity_name


class Control(models.Model):

    class IntervalType(models.TextChoices):
        TSN = 'TSN', _('Time Since New')
        TSR = 'TSR', _('Time Since Repair')
        TSO = 'TSO', _('Time Since Overhaul')
        TSI = 'TSI', _('Time Since Inspection')

    control_name = models.CharField(max_length=100, unique=True)
    interval_type = models.CharField(max_length=3, choices=IntervalType.choices, default=IntervalType.TSN)
    interval_day_count = models.IntegerField(blank=True, null=True)
    interval_cycle_count = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.control_name


class PN(models.Model):
    part_number = models.CharField(max_length=100, unique=True)
    component_part_number = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    effectivity = models.ManyToManyField(Effectivity)

    def __str__(self):
        return self.part_number


class RotablePN(PN):
    components = models.ManyToManyField(PN, related_name='+')
    controls = models.ManyToManyField(Control)


class RepairablePN(PN):
    is_serialized = models.BooleanField()


class ExpendablePN(PN):
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE)
