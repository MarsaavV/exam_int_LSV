# Generated by Django 5.1.3 on 2024-11-10 15:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cliente',
            old_name='apellido',
            new_name='Apellido',
        ),
        migrations.RenameField(
            model_name='cliente',
            old_name='dni',
            new_name='DNI',
        ),
        migrations.RenameField(
            model_name='cliente',
            old_name='nombre',
            new_name='Nombre',
        ),
    ]
