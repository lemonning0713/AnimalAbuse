# Generated by Django 3.1.1 on 2020-09-25 04:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('animalabuse', '0002_auto_20200925_0117'),
    ]

    operations = [
        migrations.AddField(
            model_name='animalabuse',
            name='county',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
    ]
