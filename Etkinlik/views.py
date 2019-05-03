from django.shortcuts import render, get_object_or_404
from .models import Etkinlik, EtkinlikMail, Mail
from django.http import JsonResponse
import json
from django.core import serializers
from .etkinlikPdf import *


def kullanici_etkinlik_cek(mail):
    etkinlikler = []
    etkinliks = EtkinlikMail.objects.filter(mail=mail)
    for etkinlik in etkinliks:
        etkinlikler.append(
            f'{etkinlik.etkinlik.baslangic_saati}-{etkinlik.etkinlik.bitis_saati}   {etkinlik.etkinlik.etkinlik_adi}    {etkinlik.etkinlik.salon}   {etkinlik.etkinlik.konusmaci_adi}')

    pdf_creates(etkinlikler, mail.email)


def emailCreate(email):
    try:
        mail = get_object_or_404(Mail, email=email)
        return mail
    except:
        mail = Mail()
        mail.email = email
        mail.save()
        return mail


def get_etkinlik(ID):
    etkinlik = get_object_or_404(Etkinlik, Id=int(ID))
    return etkinlik


def etkinlik_all(request):
    try:
        data = serializers.serialize('json', Etkinlik.objects.all())
        return JsonResponse(data, safe=False)
    except:
        return JsonResponse({'status': 0}, safe=False)


def etkinlik_mail(request):
    email = request.GET.get('email')
    mail = emailCreate(email)

    etkinlikId = (request.GET.get('etkinlik'))

    etkinliks = [get_etkinlik(ID) for ID in etkinlikId.split(',')]

    for etkinlik in etkinliks:
        mails_ = EtkinlikMail.objects.filter(mail=mail, etkinlik=etkinlik)
        if not mails_:
            etkinlik_mails = EtkinlikMail()
            etkinlik_mails.mail = mail
            etkinlik_mails.etkinlik = etkinlik
            etkinlik_mails.save()

    kullanici_etkinlik_cek(mail)
    return JsonResponse({'status': 'Tamamdır Abi'}, safe=False)


def home_view(request):
    return render(request, 'home.html')
