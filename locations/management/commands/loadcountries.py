import pandas as pd
from django.core.management.base import BaseCommand
from locations.models import Countries

class Command(BaseCommand):
    help = 'Script for load countries to DB'
    excel_path = "D:/Library/Desktop/SAEF/paises.xlsx"

    def handle(self, *args, **kwargs):
        df = pd.read_excel(self.excel_path)
        for _, row in df.iterrows():
            if not Countries.objects.filter(co_iso_num = row.isoNum).exists():
                Countries.objects.create(co_iso_num = row.isoNum,
                                         co_iso_al2 = row.alphaii if type(row.alphaii) is not float else 'NA',
                                         co_iso_al3 = row.alphaiii,
                                         co_call_code = row.callcode,
                                         co_name = row.nombre)
                print(row.nombre)