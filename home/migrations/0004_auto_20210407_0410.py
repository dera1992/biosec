# Generated by Django 3.2 on 2021-04-07 03:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_historicalemployee'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='email',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='historicalemployee',
            name='email',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]