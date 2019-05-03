from django.contrib import admin

from .models import User


class UserAdmin(admin.ModelAdmin):
    # list_display = ['email', 'name', 'admin']  # Listelerken Göstermek için
    # list_display_links = ['name']  # link oluşturmak için
    # list_filter = ['email', ]  # Filtreleme yapmak için

    # list_editable = ['ogretmen_mi', 'admin']

    class Meta:
        model = User


admin.site.register(User, UserAdmin)
