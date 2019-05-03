from django.db import models


class Etkinlik(models.Model):
    Id = models.AutoField(primary_key=True)
    tarih = models.DateTimeField()
    bitis_saati = models.CharField(max_length=5, verbose_name='bitiş')
    etkinlik_adi = models.CharField(max_length=128, verbose_name='Etkinlik')
    konusmaci_adi = models.CharField(max_length=128, verbose_name='Konuşmacı')
    salon = models.CharField(max_length=30)


class Mail(models.Model):
    Id = models.AutoField(primary_key=True)
    email = models.EmailField()
