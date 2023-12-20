# Generated by Django 4.2.5 on 2023-12-14 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('church_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Special_Masses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_name', models.CharField(max_length=100)),
                ('date', models.DateField()),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
                ('description', models.CharField(max_length=1000)),
            ],
        ),
    ]