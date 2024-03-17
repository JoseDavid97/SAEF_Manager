from django.shortcuts import render
from .models import Parameters
from django.http.response import JsonResponse
from django.views.generic import ListView

class showParameters(ListView):
    model = Parameters
    paginate_by = 20

def createParameter(request):

    if request.GET.get('action') == "add":
        parob = Parameters.objects.create(par_name = request.GET.get('name'),
                                          par_value = request.GET.get('value'),
                                          par_isnumber = request.GET.get('isnumber'),
                                          par_desc = request.GET.get('desc'))
        
    elif request.GET.get('action') == "edit": 
        parobQS = Parameters.objects.filter(par_id = request.GET.get('parameter'))
        parobQS.update(par_name = request.GET.get('name'),
                       par_value = request.GET.get('value'),
                       par_isnumber = request.GET.get('isnumber'),
                       par_desc = request.GET.get('desc'))
        parob = parobQS.first()

    data = {'id': parob.par_id,
            'name': parob.par_name,
            'value': parob.par_value,
            'desc': parob.par_desc}

    return JsonResponse(data, status=200)

def getParameter(request):

    return JsonResponse(data, status=200)

def deleteParameter(request):

    return JsonResponse({'status':True}, status=200)