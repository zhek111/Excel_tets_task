import os

import django
from django.db.models import Sum

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "djangoProject1.settings")
django.setup()

from sheet.models import Sheet, Total

from datetime import datetime


def calculate_totals():
    start_date = datetime(2023, 3, 1)
    end_date = datetime(2023, 3, 20)

    sheets = Sheet.objects.select_related('fact').filter(
        date__range=[start_date, end_date])

    totals = sheets.values('date').annotate(
        qoil_total=Sum('fact__qoil__data1') + Sum('fact__qoil__data2'),
        qliq_total=Sum('fact__qliq__data1') + Sum('fact__qliq__data2'))

    totals_to_create = [
        Total(date=total['date'], qoil_total=total['qoil_total'],
              qliq_total=total['qliq_total']) for total in totals]

    Total.objects.bulk_create(totals_to_create, ignore_conflicts=True)
