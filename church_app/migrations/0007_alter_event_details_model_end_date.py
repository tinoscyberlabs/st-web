# Generated by Django 4.2.5 on 2023-12-16 07:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('church_app', '0006_alter_event_details_model_end_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event_details_model',
            name='end_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
