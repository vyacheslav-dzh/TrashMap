# Generated by Django 3.2.7 on 2021-12-03 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CamMarker',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('c_name', models.CharField(max_length=255)),
                ('c_cord', models.CharField(max_length=255)),
                ('c_mode', models.IntegerField()),
                ('c_date', models.DateTimeField()),
            ],
        ),
    ]