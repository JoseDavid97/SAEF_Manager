from django.db import models
from locations.models import Locations

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