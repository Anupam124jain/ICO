# Generated by Django 2.1 on 2018-09-11 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_auto_20180911_1244'),
    ]

    operations = [
        migrations.CreateModel(
            name='WhitePaper',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('whitepaper', models.FileField(upload_to='whitepapers')),
            ],
            options={
                'verbose_name': 'WhitePaper',
                'verbose_name_plural': 'WhitePapers',
            },
        ),
        migrations.AlterModelOptions(
            name='kyc',
            options={'verbose_name_plural': 'Kyc'},
        ),
        migrations.AlterModelOptions(
            name='userdetails',
            options={'verbose_name_plural': 'UserDetails'},
        ),
    ]
