# Generated by Django 2.2 on 2022-03-23 08:47

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0006_auto_20220323_1249'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shopuser',
            name='activation_key_expires',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 3, 25, 8, 47, 59, 842315, tzinfo=utc), null=True),
        ),
    ]
