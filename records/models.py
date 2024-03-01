from django.db import models
from locations.models import Locations

# Create your models here.
class Consup_Master(models.Model):
    pc_id = models.AutoField(primary_key = True)
    lo_id = models.ForeignKey(Locations, on_delete = models.CASCADE)
    pc_date = models.DateField()
    pc_hour = models.SmallIntegerField()
    pc_kWh = models.DecimalField(max_digits = 7, decimal_places = 2, null = True)
    pc_kVARhL = models.DecimalField(max_digits = 7, decimal_places = 2, null = True)
    pc_kVARhC = models.DecimalField(max_digits = 7, decimal_places = 2, null = True)
    pc_kVARhP = models.DecimalField(max_digits = 7, decimal_places = 2, null = True)
    pc_pf = models.DecimalField(max_digits = 3, decimal_places = 2, null = True)

class Consup_detail(models.Model):
    cd_id = models.AutoField(primary_key = True)
    cm_id = models.ForeignKey(Consup_Master, on_delete = models.CASCADE)
    