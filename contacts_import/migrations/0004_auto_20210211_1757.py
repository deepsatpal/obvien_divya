# Generated by Django 3.1.4 on 2021-02-11 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts_import', '0003_contactsocialplatform'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='city',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='job',
            name='country',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
