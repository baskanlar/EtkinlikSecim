# Generated by Django 2.2.1 on 2019-05-03 09:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Etkinlik', '0002_mail'),
    ]

    operations = [
        migrations.CreateModel(
            name='EtkinlikMail',
            fields=[
                ('Id', models.AutoField(primary_key=True, serialize=False)),
                ('Mail', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Mail', to='Etkinlik.Mail', verbose_name='Mail')),
                ('etkinlik', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Etkinlik', to='Etkinlik.Etkinlik', verbose_name='Etkinlik')),
            ],
        ),
    ]