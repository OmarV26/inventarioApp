# Generated by Django 5.0.1 on 2024-10-06 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventarioApp', '0003_usuarios_rol'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pantalones',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('color', models.CharField(max_length=100)),
                ('talla', models.CharField(max_length=50)),
                ('categoria', models.CharField(max_length=100)),
                ('precio', models.IntegerField()),
                ('stock', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Zapatos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('color', models.CharField(max_length=100)),
                ('talla', models.CharField(max_length=50)),
                ('categoria', models.CharField(max_length=200)),
                ('precio', models.IntegerField()),
                ('stock', models.IntegerField()),
            ],
        ),
    ]
