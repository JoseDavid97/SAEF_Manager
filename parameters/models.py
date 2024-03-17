from django.db import models

# Create your models here.
class Parameters(models.Model):
    par_id = models.AutoField(primary_key=True)
    par_name = models.CharField(max_length = 50, unique=True)
    par_value = models.TextField()
    par_isnumber = models.BooleanField()
    par_desc = models.CharField(max_length = 200)