# Generated by Django 2.1 on 2018-09-10 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20180907_0555'),
    ]

    operations = [
        migrations.AddField(
            model_name='userdetails',
            name='email_confirmed',
            field=models.BooleanField(default=False),
        ),
    ]
