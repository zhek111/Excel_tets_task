import os

import django
import openpyxl

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "djangoProject1.settings")
django.setup()

from django.db import transaction

from sheet.models import Company, Quantity, Scores, Sheet, Total

from datetime import datetime, timedelta


def parse_excel_file(file_path):
    wb = openpyxl.load_workbook(file_path)
    ws = wb.active

    with transaction.atomic():
        for row_num, row in enumerate(ws.iter_rows(min_row=4), start=1):
            company_title = row[1].value

            company, _ = Company.objects.get_or_create(title=company_title)

            qliq_fact_quantity = Quantity.objects.create(data1=row[2].value,
                                                         data2=row[3].value)
            qoil_fact_quantity = Quantity.objects.create(data1=row[4].value,
                                                         data2=row[5].value)
            qliq_forecast_quantity = Quantity.objects.create(
                data1=row[6].value, data2=row[7].value)
            qoil_forecast_quantity = Quantity.objects.create(
                data1=row[8].value, data2=row[9].value)

            qliq_fact_scores = Scores.objects.create(qliq=qliq_fact_quantity,
                                                     qoil=qoil_fact_quantity,
                                                     SCORE_TYPE_CHOICES='fact')
            qliq_forecast_scores = Scores.objects.create(
                qliq=qliq_forecast_quantity, qoil=qoil_forecast_quantity,
                SCORE_TYPE_CHOICES='forecast')

            Sheet.objects.create(
                company=company,
                fact=qliq_fact_scores,
                forecast=qliq_forecast_scores,
                date=datetime(2023, 3, 1) + timedelta(days=row_num - 1)
            )
