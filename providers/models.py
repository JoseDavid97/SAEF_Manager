from django.db import models
from locations.models import Locations

class Parameters(models.Model):
    par_id = models.AutoField(primary_key = True)
    lc_id = models.ForeignKey(Locations, on_delete = models.CASCADE)
    par_name = models.CharField(max_length = 50, unique=True)
    par_value_number = models.FloatField(null = True)
    par_value_string = models.TextField(null = True)
    par_isnumber = models.BooleanField()
    par_desc = models.CharField(max_length = 200)

    def getParameter(self, name):
        param = self.objects.get(par_name = name)
        if param.par_isnumber:
            return param.par_value_number
        else:
            return param.par_value_string

class ActionDTypes(models.Model):
    at_id = models.AutoField(primary_key = True)
    at_name = models.CharField(max_length = 50)
    at_desc = models.CharField(max_length = 200)

class ActionMTypes(models.Model):
    at_id = models.AutoField(primary_key = True)
    at_name = models.CharField(max_length = 50)
    at_desc = models.CharField(max_length = 200)

class ActionsMaster(models.Model):
    am_id = models.AutoField(primary_key = True)
    lo_id = models.ForeignKey(Locations, on_delete = models.CASCADE)
    am_type = models.ForeignKey(ActionMTypes, on_delete = models.CASCADE)
    am_desc = models.CharField(max_length = 200)

class ActionsDetail(models.Model):
    ad_id = models.AutoField(primary_key = True)
    am_id = models.ForeignKey(ActionsMaster, on_delete = models.CASCADE)
    ad_seq = models.IntegerField()
    ad_type = models.ForeignKey(ActionDTypes, on_delete = models.CASCADE)
    ad_sc_id = models.CharField(max_length = 50, null = True)
    ad_sc_name = models.CharField(max_length = 50, null = True)
    ad_sc_xp = models.CharField(max_length = 200, null = True)
    ad_sc_val = models.CharField(max_length = 200, null = True)

hola = {"pc_kWh":"Activa",
        "pc_kVARhL":"Reactiva Inductiva",
        "pc_kVARhC":"Reactiva Capacitiva",
        "pc_kVARhP":"Reactiva Inductiva Penalizada",
        "pc_pf":"Factor de Potencia"}