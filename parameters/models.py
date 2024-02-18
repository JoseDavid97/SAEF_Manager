from django.db import models

# Create your models here.
class Parameters(models.Model):
    par_id = models.AutoField(primary_key=True)
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
        
    def setParameter(self, name, value):
        param = self.objects.get(par_name = name)
        if param.par_isnumber:
            param.par_value_number = value
        else:
            param.par_value_string = value
        param.save()