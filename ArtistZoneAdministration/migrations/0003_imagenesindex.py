# Generated by Django 3.2.4 on 2021-07-14 06:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ArtistZoneAdministration', '0002_task'),
    ]

    operations = [
        migrations.CreateModel(
            name='ImagenesIndex',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=200)),
                ('imagen', models.ImageField(null=True, upload_to='imagenes')),
            ],
        ),
    ]