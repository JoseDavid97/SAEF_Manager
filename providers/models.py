from django.db import models

# Create your models here.
class Providers(models.Model):
    pr_id = models.AutoField(primary_key = True)
    pr_name = models.CharField(max_length = 100)
    lo_id = models.OneToOneField("locations.Locations", on_delete = models.CASCADE)