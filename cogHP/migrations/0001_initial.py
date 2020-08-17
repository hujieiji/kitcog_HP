# Generated by Django 3.0.6 on 2020-06-28 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Achivement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=500)),
                ('year', models.CharField(max_length=50)),
                ('title', models.CharField(max_length=1000)),
                ('journal', models.CharField(max_length=200)),
                ('pages', models.CharField(default='pp., blank=True', max_length=50)),
                ('published_year', models.CharField(blank=True, max_length=50)),
                ('review', models.BooleanField(verbose_name='査読の有無')),
            ],
        ),
        migrations.CreateModel(
            name='Recruiting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('apply_link', models.URLField()),
                ('period_start', models.DateField()),
                ('period_end', models.DateField()),
                ('duration_hour', models.DurationField()),
                ('place', models.CharField(max_length=200)),
                ('experimenter', models.CharField(max_length=200)),
                ('exp_grade', models.CharField(max_length=50, verbose_name='実験者の学年')),
                ('reward', models.CharField(max_length=200)),
                ('precautions', models.TextField(default='※事前アンケートあり（アンケートの結果，実験参加者として採用されない場合がございます．ご了承ください．）')),
            ],
        ),
    ]
