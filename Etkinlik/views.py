from django.shortcuts import render
from .models import Etkinlik, EtkinlikMail, Mail
from django.http import JsonResponse
import json
from django.core import serializers


def home_view(request):
    return render(request, 'home.html')


def mail_create_api(request):
    try:
        mail = Mail()
        mail.email = request.GET.get('email')
        mail.save()
        print(mail.Id)
        return mail.Id
    except IntegrityError:

        mail = Mail.objects.filter(email=request.GET.get('email'))
        return mail.Id


def Etkinlik_all(request):
    try:
        data = serializers.serialize('json', Etkinlik.objects.all())
        return JsonResponse({'status': 1, 'data': data}, safe=False)
    except:
        return JsonResponse({'status': 0}, safe=False)
