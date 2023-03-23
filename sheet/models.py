from django.db import models


class Company(models.Model):
    title = models.CharField(max_length=255)


class Quantity(models.Model):
    data1 = models.IntegerField()
    data2 = models.IntegerField()


class Scores(models.Model):
    Scores = [
        ('fact', 'Fact'),
        ('forecast', 'Forecast'),
    ]

    qliq = models.ForeignKey(Quantity, on_delete=models.CASCADE,
                             related_name="qliq_scores")
    qoil = models.ForeignKey(Quantity, on_delete=models.CASCADE,
                             related_name="qoil_scores")
    SCORE_TYPE_CHOICES = models.CharField(choices=Scores, max_length=10)


from django.db import models


class Sheet(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    fact = models.ForeignKey(Scores, on_delete=models.CASCADE,
                             related_name="fact_sheet")
    forecast = models.ForeignKey(Scores, on_delete=models.CASCADE,
                                 related_name="forecast_sheet")
    date = models.DateField(blank=True, null=True)




class Total(models.Model):
    date = models.DateField()
    qoil_total = models.IntegerField(blank=True, null=True)
    qliq_total = models.IntegerField(blank=True, null=True)

