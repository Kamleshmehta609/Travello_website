# Generated by Django 4.0.6 on 2022-07-27 17:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('travello', '0002_destination_summ'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='destination',
            name='summ',
        ),
    ]
