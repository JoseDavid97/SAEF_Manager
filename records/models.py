from django.db import models
from locations.models import Locations
from consumers.models import Meters
from generators.models import Generators

# Create your models here.
class Consup_Master(models.Model):
    pc_id = models.AutoField(primary_key = True)
    pc_date = models.DateField()
    pc_hour = models.SmallIntegerField()

class Consup_provider(models.Model):
    cd_id = models.AutoField(primary_key = True)
    lo_id = models.ForeignKey(Locations, on_delete = models.CASCADE)
    cm_id = models.ForeignKey(Consup_Master, on_delete = models.CASCADE)

    pc_kWh = models.DecimalField(max_digits = 7, decimal_places = 2, null = True)
    pc_kVARhL = models.DecimalField(max_digits = 7, decimal_places = 2, null = True)
    pc_kVARhC = models.DecimalField(max_digits = 7, decimal_places = 2, null = True)
    pc_kVARhP = models.DecimalField(max_digits = 7, decimal_places = 2, null = True)
    pc_pf = models.DecimalField(max_digits = 3, decimal_places = 2, null = True)

class Consup_meter(models.Model):
    cd_id = models.AutoField(primary_key = True)
    mt_id = models.ForeignKey(Meters, on_delete = models.CASCADE)
    cm_id = models.ForeignKey(Consup_Master, on_delete = models.CASCADE)

    pc_kWh = models.DecimalField(max_digits = 7, decimal_places = 2, null = True)
    pc_kVARhL = models.DecimalField(max_digits = 7, decimal_places = 2, null = True)
    pc_kVARhC = models.DecimalField(max_digits = 7, decimal_places = 2, null = True)
    pc_kVARhP = models.DecimalField(max_digits = 7, decimal_places = 2, null = True)
    pc_pf = models.DecimalField(max_digits = 3, decimal_places = 2, null = True)

class Consup_generator(models.Model):
    cd_id = models.AutoField(primary_key = True)
    gn_id = models.ForeignKey(Generators, on_delete = models.CASCADE)
    cm_id = models.ForeignKey(Consup_Master, on_delete = models.CASCADE)

    pc_kWh = models.DecimalField(max_digits = 7, decimal_places = 2, null = True)
    pc_kVARhL = models.DecimalField(max_digits = 7, decimal_places = 2, null = True)
    pc_kVARhC = models.DecimalField(max_digits = 7, decimal_places = 2, null = True)
    pc_kVARhP = models.DecimalField(max_digits = 7, decimal_places = 2, null = True)
    pc_pf = models.DecimalField(max_digits = 3, decimal_places = 2, null = True)