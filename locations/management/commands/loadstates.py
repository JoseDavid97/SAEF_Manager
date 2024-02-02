import pandas as pd
from django.core.management.base import BaseCommand
from locations.models import Countries, States

class Command(BaseCommand):
    help = 'Script for load states to DB'
    excel_path = "D:/Library/Desktop/SAEF/worldcities.xlsx"

    def handle(self, *args, **kwargs):
        df = pd.read_excel(self.excel_path)
        df = df.drop(columns = ['city'])
        df = df.drop_duplicates()
        
        for country in Countries.objects.all():
            cdf = df[df['iso2'] == country.co_iso_al2]
            
            for _, row in cdf.iterrows():
                if not States.objects.filter(st_name = row.adminname).exists():
                    States.objects.create(co_iso_num = country,
                                          st_name = row.adminname)
                    print(row.adminname)