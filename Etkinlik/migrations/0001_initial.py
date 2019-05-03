# Generated by Django 2.2.1 on 2019-05-03 10:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Etkinlik',
            fields=[
                ('Id', models.AutoField(primary_key=True, serialize=False)),
                ('tarih', models.DateTimeField()),
                ('bitis_saati', models.CharField(max_length=5, verbose_name='bitiş')),
                ('etkinlik_adi', models.CharField(max_length=128, verbose_name='Etkinlik')),
                ('konusmaci_adi', models.CharField(max_length=128, verbose_name='Konuşmacı')),
                ('salon', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Mail',
            fields=[
                ('Id', models.AutoField(primary_key=True, serialize=False)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('mail_olusturma', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='EtkinlikMail',
            fields=[
                ('Id', models.AutoField(primary_key=True, serialize=False)),
                ('etkinlik', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Etkinlik', to='Etkinlik.Etkinlik', verbose_name='Etkinlik')),
                ('mail', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Mail', to='Etkinlik.Mail', verbose_name='Mail')),
            ],
        ),
    ]
