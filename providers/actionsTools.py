from .models import ActionsMaster, ActionsDetail

class Actioner:

    def __init__(self, Location):
        self.lo = Location

    def getEvents(self, action):
        AM = ActionsMaster.objects.get(lo_id = self.lo, am_type__at_name = action)
        return ActionsDetail.objects.filter(am_id = AM).order_by('ad_seq')