# Generated by Django 4.1.7 on 2023-03-29 19:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0002_teacher'),
    ]

    operations = [
        migrations.RenameField(
            model_name='course',
            old_name='duraion',
            new_name='duration',
        ),
    ]
