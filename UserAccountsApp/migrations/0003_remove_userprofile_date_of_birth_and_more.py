# Generated by Django 4.0.2 on 2022-02-27 19:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('UserAccountsApp', '0002_userprofile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='date_of_birth',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='f_name',
        ),
    ]
