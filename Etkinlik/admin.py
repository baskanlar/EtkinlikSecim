from django.contrib import admin

# Register your models here.
from .models import Etkinlik, Mail, EtkinlikMail


class EtkinlikAdmin(admin.ModelAdmin):
    list_display = ['Id', 'baslangic_saati', 'bitis_saati', 'etkinlik_adi', 'konusmaci_adi', 'salon',
                    'tarih', ]  # Listelerken Göstermek için

    list_editable = ['etkinlik_adi', 'baslangic_saati', 'bitis_saati', 'konusmaci_adi', 'salon', 'tarih']

    class Meta:
        model = Etkinlik


class MainAdmin(admin.ModelAdmin):
    list_display = ['Id', 'email']  # Listelerken Göstermek için

    class Meta:
        model = Mail


class EtkinlikMailAdmin(admin.ModelAdmin):
    list_display = ['Id', 'etkinlik', 'mail']
    list_display_links = ['Id']

    class Meta:
        model = EtkinlikMail


admin.site.register(Etkinlik, EtkinlikAdmin)
admin.site.register(Mail, MainAdmin)
admin.site.register(EtkinlikMail, EtkinlikMailAdmin)
