# Generated by Django 4.0.1 on 2022-01-25 19:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='pub_date',
            field=models.DateField(verbose_name='date published'),
        ),
    ]
