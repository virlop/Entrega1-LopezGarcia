# Generated by Django 4.0.4 on 2022-05-25 22:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('familia', '0003_persona_altura'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mascota',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('fecha_adopcion', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Gato',
            fields=[
                ('mascota_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='familia.mascota')),
                ('color_pelaje', models.CharField(max_length=100)),
            ],
            bases=('familia.mascota',),
        ),
        migrations.CreateModel(
            name='Perro',
            fields=[
                ('mascota_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='familia.mascota')),
                ('raza', models.CharField(max_length=100)),
            ],
            bases=('familia.mascota',),
        ),
    ]
