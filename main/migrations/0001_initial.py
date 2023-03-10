# Generated by Django 4.1.7 on 2023-02-21 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Frase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('frase', models.CharField(max_length=60)),
                ('pista_inicial', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usuario', models.CharField(max_length=30)),
                ('puntuacion', models.PositiveIntegerField(blank=True, null=True)),
                ('puntos_iniciales', models.PositiveIntegerField(default=200)),
            ],
        ),
    ]
