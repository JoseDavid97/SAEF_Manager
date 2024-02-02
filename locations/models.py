from django.db import models

# Create your models here.
class Countries(models.Model):
    co_iso_num = models.CharField(max_length = 3, primary_key = True)
    co_iso_al2 = models.CharField(max_length = 2)
    co_iso_al3 = models.CharField(max_length = 3)
    co_call_code = models.CharField(max_length = 5)
    co_name = models.CharField(max_length = 50)

class States(models.Model):
    st_code = models.AutoField(primary_key = True)
    co_iso_num = models.ForeignKey("Countries", on_delete=models.CASCADE)
    st_name = models.CharField(max_length = 100)

class Cities(models.Model):
    ct_code = models.AutoField(primary_key = True)
    st_code = models.ForeignKey("States", on_delete=models.CASCADE)
    ct_name = models.CharField(max_length = 100)

class Locations(models.Model):
    lo_id = models.AutoField(primary_key = True)
    lo_name = models.CharField(max_length = 100)
    lo_addrl1 = models.CharField(max_length = 100)
    lo_addrl2 = models.CharField(max_length = 100)
    ct_code = models.ForeignKey("Cities", on_delete=models.DO_NOTHING)