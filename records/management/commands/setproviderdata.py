import json
import pandas as pd
from os.path import join
from datetime import date
from django.core.management.base import BaseCommand, CommandError
from records.models import Consup_Master
from providers.models import Parameters
from locations.models import Locations
from SAEF_Manager.settings import BASE_DIR

class Command(BaseCommand):
    help = 'Script for set records from energy providers'
    initRow = 1
    initCol = 2
    
    def add_arguments(self, parser): 
        parser.add_argument("provider", nargs=1, type=int, help='Iternal provider ID')
        parser.add_argument("-d", '--date', help='Optional date')
        parser.add_argument("--billing",action="store_true", help="set billing")
        parser.add_argument("--consuption",action="store_true", help="set consuption")

    def handle(self, *args, **kwargs):
        lo_id = kwargs['provider'][0]
        loobQS = Locations.objects.filter(lo_id = lo_id)

        if loobQS.exists():
            loob = loobQS.first()
            if not (kwargs["billing"] or kwargs["consuption"]):
                raise CommandError(f"Please add action \"--billing\" or \"--consuption\"")
            elif kwargs["billing"]:
                self.stdout.write("Not released")
            elif kwargs["consuption"]:

                if kwargs['date']:
                    dateNS = kwargs['date'].split(' ')
                    Y, M = dateNS[0], dateNS[1]
                else:
                    today = date.today()
                    Y, M = today.year, today.month

                    if M > 1:
                        M = M - 1
                        if M < 10: M = f'0{M}'
                    else:
                        M = 12
                        Y = Y - 1

                fileNameFormat = Parameters.objects.get(par_name = 'consuption_filename').par_value_string
                fileSheets = json.loads(Parameters.objects.get(par_name = 'consuptionfile_sheets').par_value_string)
                file = join(BASE_DIR, 'downloads', fileNameFormat.format(Y, M, Y, M))

                for var, sheet in fileSheets.items():
                    try:
                        df = pd.read_excel(file, sheet_name = sheet)
                    except:
                        CommandError(f"Error reading \"{file}\" with sheet named \"{sheet}\"")
                    columns = df.columns
                    for index, row in df.iterrows():
                        if index >= self.initRow:
                            recDateSet = row[columns[self.initCol - 1]].split('/')
                            recDate = date(year = int(recDateSet[2]), month = int(recDateSet[1]), day = int(recDateSet[0]))
                            
                            for hAux in range(self.initCol, self.initCol + 24):
                                hour = hAux - self.initCol
                                val = Consup_Master.objects.filter(lo_id = loob,
                                                                   pc_date = recDate,
                                                                   pc_hour = hour)
                                
                                if val.exists():
                                    exec(f'val.update({var} = row[columns[hAux]])')
                                else:
                                    exec(f"""Consup_Master.objects.create(lo_id = prob,
                                                                          pc_date = recDate,
                                                                          pc_hour = hour,
                                                                          {var} = row[columns[hAux]])""")
        else:
            raise CommandError(f"Location with ID \"{lo_id}\" not found")
        