# Generated by Django 3.0.6 on 2020-06-28 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cogHP', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='achivement',
            name='pages',
            field=models.CharField(blank=True, default='pp.', max_length=50),
        ),
    ]
