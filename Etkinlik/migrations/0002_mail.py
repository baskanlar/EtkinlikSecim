# Generated by Django 2.2.1 on 2019-05-03 08:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Etkinlik', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mail',
            fields=[
                ('Id', models.AutoField(primary_key=True, serialize=False)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
    ]