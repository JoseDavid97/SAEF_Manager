import pandas as pd
from django.core.management.base import BaseCommand
from locations.models import Countries, States, Cities

class Command(BaseCommand):
    help = 'Script for load states to DB'
    excel_path = "D:/Library/Desktop/SAEF/worldcities.xlsx"

    def handle(self, *args, **kwargs):
        df = pd.read_excel(self.excel_path)
        
        for country in Countries.objects.all():
            for state in States.objects.filter(co_iso_num = country):
                cdf = df[(df['iso2'] == country.co_iso_al2) & (df['adminname'] == state.st_name)]
                for _, row in cdf.iterrows():
                    if not Cities.objects.filter(ct_name = row.city).exists():
                        Cities.objects.create(st_code = state,
                                              ct_name = row.city)
                        print(row.city)