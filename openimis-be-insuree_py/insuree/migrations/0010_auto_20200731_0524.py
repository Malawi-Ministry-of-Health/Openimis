# Generated by Django 3.0.3 on 2020-07-31 05:24
from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('insuree', '0009_familymutation_insureemutation'),
    ]

    operations = [
        migrations.RunSQL('ALTER TABLE [tblInsuree] ADD [JsonExt] TEXT'
                          if settings.MSSQL else
                          'ALTER TABLE "tblInsuree" ADD "JsonExt" jsonb'),
        migrations.RunSQL('ALTER TABLE [tblFamilies] ADD [JsonExt] TEXT'
                          if settings.MSSQL else
                          'ALTER TABLE "tblFamilies" ADD "JsonExt" jsonb'),
    ]