from django.db import models
from locations.models import Locations

# Create your models here.
class Meters(models.Model):
    mt_id = models.AutoField(primary_key = True)
    lo_id = models.ForeignKey(Locations, on_delete = models.CASCADE)
    mt_name = models.CharField(max_length = 100)
    mt_url = models.URLField()