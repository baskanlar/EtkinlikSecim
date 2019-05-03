from django.db import models


class Etkinlik(models.Model):
    Id = models.AutoField(primary_key=True)
    tarih = models.DateTimeField()
    etkinlik_adi = models.CharField(max_length=128, verbose_name='Etkinlik')
    konusmaci_adi = models.CharField(max_length=128, verbose_name='Konuşmacı')
    salon = models.CharField(max_length=30)
