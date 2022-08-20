# Generated by Django 3.1.4 on 2021-03-05 06:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contacts_import', '0005_job_area'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('search_history', '0004_auto_20210224_1558'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactviewhistory',
            name='contact',
            field=models.OneToOneField(default='', on_delete=django.db.models.deletion.CASCADE, to='contacts_import.contact'),
        ),
        migrations.AlterField(
            model_name='contactviewhistory',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='SearchHistory',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('search_term', models.CharField(default='', max_length=150)),
                ('filters', models.CharField(max_length=1000, null=True)),
                ('filter_weights', models.CharField(max_length=1000, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'search_history',
            },
        ),
    ]