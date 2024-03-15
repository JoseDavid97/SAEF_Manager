from django.db import models
from locations.models import Locations

# Create your models here.
class Generators(models.Model):
    gn_id = models.AutoField(primary_key = True)
    lo_id = models.ForeignKey(Locations, on_delete = models.CASCADE)
    gn_name = models.CharField(max_length = 100)
    gn_url = models.URLField()