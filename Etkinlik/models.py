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
    email = models.EmailField(unique=True)
    mail_olusturma = models.DateField(auto_now_add=True)


class EtkinlikMail(models.Model):
    Id = models.AutoField(primary_key=True)
    etkinlik = models.ForeignKey('Etkinlik.Etkinlik', verbose_name='Etkinlik', on_delete=models.CASCADE,
                                 related_name='Etkinlik')
    mail = models.ForeignKey('Etkinlik.Mail', verbose_name='Mail', on_delete=models.CASCADE, related_name='Mail')
