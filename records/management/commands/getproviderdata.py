from datetime import datetime
from django.core.management.base import BaseCommand, CommandError
from locations.models import Locations
from providers.actionsTools import Actioner
from records.webscrapping import Scrapper
from SAEF_Manager.settings import DOWNLOAD_DIR

class Command(BaseCommand):
    help = 'Script for get records and billing from energy providers'

    def add_arguments(self, parser): 
        parser.add_argument("location", nargs=1, type=int, help='Iternal Location ID')
        parser.add_argument("--billing",action="store_true", help="Download billing")
        parser.add_argument("--consuption",action="store_true", help="Download consuption")
        parser.add_argument("-d", '--date', help='Optional date')

    def handle(self, *args, **kwargs):
        lo_id = kwargs['provider'][0]
        loobQS = Locations.objects.filter(lo_id = lo_id)

        if loobQS.exists():
            if not (kwargs["billing"] or kwargs["consuption"]):
                raise CommandError(f"Please add action \"--billing\" or \"--consuption\"")
            
            loob = loobQS.first()
            
            AC = Actioner(loob)
            sc = Scrapper(loob.pr_webacc, d_path = str(DOWNLOAD_DIR), headless = False)
            
            sc.eventList(AC.getEvents('signin'))

            if kwargs['date']:
                dateNS = kwargs['date'].split(' ')
                Y, M = dateNS[0], dateNS[1]
                date = datetime(year = int(Y), month = int(M), day = 1)
            else:
                date = None
            
            if kwargs["billing"]:
                self.stdout.write(f"Getting billing from {loob.pr_name}")
                sc.eventList(AC.getEvents('getbilling'), optionalDate = date)
            
            if kwargs["consuption"]:
                self.stdout.write(f"Getting consuption from {loob.pr_name}")
                sc.eventList(AC.getEvents('getconsuption'), optionalDate = date)

            sc.eventList(AC.getEvents('signout'))

            sc.close()

            self.stdout.write(self.style.SUCCESS(f"Records downloaded for {loob.pr_name}"))
        else:
            raise CommandError(f"Location with ID \"{lo_id}\" not found")