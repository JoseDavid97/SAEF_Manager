from django.shortcuts import render
from .models import Parameters

def showParameters(request):
    data = []
    
    for param in Parameters.objects.all():
        data.append({'par_id': param.par_id,
                     'par_name': param.par_name,
                     'par_value': param.par_value_number if param.par_isnumber else param.par_value_string,
                     'par_desc': param.par_desc})
    
    return render(request, "parameters/parameters_list.html", {'object_list': data})