# Generated by Django 4.1.4 on 2022-12-09 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserTag',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('contact_id', models.IntegerField()),
                ('user_id', models.IntegerField()),
                ('name', models.CharField(max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'User_tags',
            },
        ),
    ]
