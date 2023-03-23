import os

import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "djangoProject1.settings")
django.setup()


from sheet.models import Sheet, Total

from datetime import datetime, timedelta


def calculate_totals():
    start_date = datetime(2023, 3, 1)
    end_date = datetime(2023, 3, 20)

    while start_date <= end_date:
        qoil_total = 0
        qliq_total = 0

        sheets = Sheet.objects.filter(date=start_date)
        for sheet in sheets:
            qoil_total += sheet.fact.qoil.data1 + sheet.fact.qoil.data2
            qliq_total += sheet.fact.qliq.data1 + sheet.fact.qliq.data2

        total, _ = Total.objects.get_or_create(date=start_date)
        total.qoil_total = qoil_total
        total.qliq_total = qliq_total
        total.save()

        start_date += timedelta(days=1)