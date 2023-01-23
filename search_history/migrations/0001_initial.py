# Generated by Django 4.1.4 on 2022-12-09 09:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contacts_import', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='SearchTerm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('search_term', models.CharField(max_length=150)),
                ('search_term_name', models.CharField(max_length=200)),
                ('filters', models.CharField(max_length=1000, null=True)),
                ('filter_weights', models.CharField(max_length=1000, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('users', models.ManyToManyField(related_name='search_terms', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'search_terms',
            },
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
        migrations.CreateModel(
            name='ContactViewHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('contact', models.OneToOneField(default='', on_delete=django.db.models.deletion.CASCADE, to='contacts_import.contact')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'user_contact_view_history',
            },
        ),
    ]
