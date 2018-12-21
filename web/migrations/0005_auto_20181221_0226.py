# Generated by Django 2.1.2 on 2018-12-21 02:26

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0004_auto_20181221_0221'),
    ]

    operations = [
        migrations.AlterField(
            model_name='buildlogline',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2018, 12, 21, 2, 26, 3, 831972, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='experiment',
            name='last_access',
            field=models.DateTimeField(default=datetime.datetime(2018, 12, 21, 2, 26, 3, 816466, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='run',
            name='submitted',
            field=models.DateTimeField(default=datetime.datetime(2018, 12, 21, 2, 26, 3, 826695, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='runlogline',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2018, 12, 21, 2, 26, 3, 832973, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='upload',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2018, 12, 21, 2, 26, 3, 823307, tzinfo=utc)),
        ),
    ]
