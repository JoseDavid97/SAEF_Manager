from .models import Meters
from django.http.response import JsonResponse
from locations.models import Locations
from django.views.generic import ListView

class showMeters(ListView):
    model = Meters
    paginate_by = 20

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['locations'] = Locations.objects.all().order_by("lo_name")
        return context
    
def createMeter(request):

    if request.GET.get('action') == "add":
        mtob = Meters.objects.create(lo_id = Locations.objects.get(lo_id = request.GET.get('location')),
                                     mt_name = request.GET.get('name'),
                                     mt_url = request.GET.get('url'))

    elif request.GET.get('action') == "edit": 
        mtobQS = Meters.objects.filter(mt_id = request.GET.get('meter'))
        mtobQS.update(lo_id = Locations.objects.get(lo_id = request.GET.get('location')),
                      mt_name = request.GET.get('name'),
                      mt_url = request.GET.get('url'))
        mtob = mtobQS.first()

    data = {'id':mtob.mt_id,
            'location':f'{mtob.lo_id.lo_name } - {mtob.lo_id.lo_addrl1 }, {mtob.lo_id.ct_code.ct_name }',
            'name':mtob.mt_name}

    return JsonResponse(data, status=200)

def getMeter(request):

    mtob = Meters.objects.get(mt_id = request.GET.get('meter'))

    data = {'location': str(mtob.lo_id.lo_id),
            'name': mtob.mt_name,
            'url': mtob.mt_url}

    return JsonResponse(data, status=200)

def deleteMeter(request):

    Meters.objects.filter(mt_id = request.GET.get('meter')).delete()
    
    return JsonResponse({'status':True}, status=200)