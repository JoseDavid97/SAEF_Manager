from django.views.generic import ListView
from django.http.response import JsonResponse
from locations.models import Locations
from .models import Providers
from time import sleep

class showProviders(ListView):
    model = Providers
    paginate_by = 20

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        ex_lo = self.model.objects.all().values_list("lo_id", flat=True)
        context['locations'] = Locations.objects.exclude(lo_id__in = ex_lo).order_by("lo_name")
        return context
    
def createProvider(request):

    if request.GET.get('action') == "add":
        prob = Providers.objects.create(pr_name = request.GET.get('name'),
                                        lo_id = Locations.objects.get(lo_id = request.GET.get('client')))
        
    elif request.GET.get('action') == "edit":
        probQS = Providers.objects.filter(pr_id = request.GET.get('provider'))
        probQS.update(pr_name = request.GET.get('name'),
                      lo_id = Locations.objects.get(lo_id = request.GET.get('client')))
        prob = probQS.first()

    data = {'id':prob.pr_id,
            'name':prob.pr_name,
            'client':prob.lo_id.lo_name}

    return JsonResponse(data, status=200)

def getProvider(request):

    prob = Providers.objects.get(pr_id = request.GET.get('provider'))

    data = {'name':prob.pr_name,
            'client':prob.lo_id.lo_id}

    return JsonResponse(data, status=200)

def deleteProvider(request):

    Providers.objects.filter(pr_id = request.GET.get('provider')).delete()
    
    return JsonResponse({'status':True}, status=200)