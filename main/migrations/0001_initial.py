# Generated by Django 4.1.5 on 2023-01-29 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Vehiculo',
            fields=[
                ('matricula', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('tipo', models.CharField(choices=[('Coche', 'Coche'), ('Ciclomotor', 'Ciclomotor'), ('Motocicleta', 'Motocicleta')], default='Coche', max_length=11)),
                ('chasis', models.PositiveIntegerField(unique=True)),
                ('marca', models.CharField(choices=[('Renault', 'Renault'), ('Seat', 'Seat'), ('BMW', 'BMW')], default='BMW', max_length=30)),
                ('modelo', models.CharField(max_length=40)),
                ('color', models.CharField(choices=[('Negro', 'Negro'), ('Rojo', 'Rojo'), ('Gris', 'Gris'), ('Azul', 'Azul')], default='Negro', max_length=30)),
                ('fecha_fabrica', models.DateField()),
                ('fecha_matricula', models.DateField(null=True)),
                ('fecha_baja', models.DateField(null=True)),
                ('suspendido', models.BooleanField(default=False)),
            ],
        ),
    ]