# Generated by Django 3.2.4 on 2021-07-13 03:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ArtistZoneApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='publicaciones',
            name='imagen_cuadro',
            field=models.ImageField(null=True, upload_to='cuadros'),
        ),
    ]
