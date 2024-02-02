from django.http.response import JsonResponse
from django.views.generic import ListView
from .models import Locations, Countries, States, Cities

class showLocations(ListView):
    model = Locations
    paginate_by = 20

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['countries'] = Countries.objects.all().order_by("co_name")
        return context
    
def createLocation(request):

    if request.GET.get('action') == "add":
        loob = Locations.objects.create(lo_name = request.GET.get('name'),
                                        lo_addrl1 = request.GET.get('address1'),
                                        lo_addrl2 = request.GET.get('address2'),
                                        ct_code = Cities.objects.get(ct_code = request.GET.get('city')))

    elif request.GET.get('action') == "edit": 
        loobQS = Locations.objects.filter(lo_id = request.GET.get('location'))
        loobQS.update(lo_name = request.GET.get('name'),
                      lo_addrl1 = request.GET.get('address1'),
                      lo_addrl2 = request.GET.get('address2'),
                      ct_code = Cities.objects.get(ct_code = request.GET.get('city')))
        loob = loobQS.first()

    data = {'id':loob.lo_id,
            'name':loob.lo_name,
            'address':f'{loob.lo_addrl1}, {loob.lo_addrl2}',
            'city':f'{loob.ct_code.ct_name}, {loob.ct_code.st_code.st_name}'}

    return JsonResponse(data, status=200)

def getLocation(request):

    loob = Locations.objects.get(lo_id = request.GET.get('location'))

    data = {'name': loob.lo_name,
            'address1': loob.lo_addrl1,
            'address2': loob.lo_addrl2,
            'country': loob.ct_code.st_code.co_iso_num.co_iso_num,
            'state': str(loob.ct_code.st_code.st_code),
            'city': str(loob.ct_code.ct_code)}

    return JsonResponse(data, status=200)

def deleteLocation(request):

    Locations.objects.filter(lo_id = request.GET.get('location')).delete()
    
    return JsonResponse({'status':True}, status=200)

def getStates(request):
    data = {'states':[{'value':state.st_code,'name':state.st_name} 
                       for state in States.objects.filter(co_iso_num = request.GET.get('country')).order_by('st_name')]}
    
    return JsonResponse(data, status=200)

def getCities(request):
    data = {'cities':[{'value':city.ct_code,'name':city.ct_name} 
                       for city in Cities.objects.filter(st_code = request.GET.get('state')).order_by('ct_name')]}
    
    return JsonResponse(data, status=200)