# Generated by Django 3.2.5 on 2021-07-24 23:56

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('dashboard', '0003_auto_20210724_1750'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Dashboard',
            new_name='StudentDetails',
        ),
    ]