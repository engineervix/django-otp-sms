# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('otp_sms', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='CustomSMSDevice',
            name='last_t',
            field=models.BigIntegerField(default=-1, help_text='The t value of the latest verified token. The next token must be at a higher time step.'),
            preserve_default=True,
        ),
    ]
