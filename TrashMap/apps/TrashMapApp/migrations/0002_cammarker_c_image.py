# Generated by Django 3.2.7 on 2021-12-03 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TrashMapApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cammarker',
            name='c_image',
            field=models.TextField(default='image'),
            preserve_default=False,
        ),
    ]