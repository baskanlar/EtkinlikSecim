from django.shortcuts import render, get_object_or_404
from .models import Etkinlik, EtkinlikMail, Mail
from django.http import JsonResponse
import json
from django.core import serializers


def home_view(request):
    return render(request, 'home.html')


def emailCreate(email):
    try:
        mail = get_object_or_404(Mail, email=email)
        return mail
    except:
        mail = Mail()
        mail.email = email
        mail.save()
        return mail


def etkinlik(ID):
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

    etkinliks = [etkinlik(ID) for ID in etkinlikId.split(',')]

    for etkinlikaa in etkinliks:
        etkinlik_mails = EtkinlikMail()
        etkinlik_mails.mail = mail
        etkinlik_mails.etkinlik = etkinlikaa
        etkinlik_mails.save()

    return JsonResponse({'status': 'Tamamdır Abi'}, safe=False)
