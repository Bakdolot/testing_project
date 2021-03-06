# Generated by Django 2.2.10 on 2022-01-11 09:00

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('questioning', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='survey',
            name='owner',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='survey_owner', to='questioning.Responder'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='survey',
            name='create_at',
            field=models.DateTimeField(auto_created=True, default=datetime.datetime(2022, 1, 11, 9, 0, 50, 302456, tzinfo=utc), verbose_name='created date time'),
        ),
        migrations.AlterField(
            model_name='survey',
            name='end_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 1, 21, 9, 0, 50, 302420, tzinfo=utc), verbose_name='end date time'),
        ),
        migrations.AlterField(
            model_name='survey',
            name='start_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 1, 11, 9, 0, 50, 302388, tzinfo=utc), verbose_name='start date time'),
        ),
    ]
