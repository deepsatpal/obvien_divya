# Generated by Django 3.1.4 on 2021-01-20 11:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('middle_name', models.CharField(max_length=50, null=True)),
                ('last_name', models.CharField(max_length=50, null=True)),
                ('photo', models.CharField(max_length=500, null=True)),
                ('country', models.CharField(max_length=50, null=True)),
                ('city', models.CharField(max_length=50, null=True)),
                ('zip_code', models.CharField(max_length=50, null=True)),
                ('street_address', models.CharField(max_length=500, null=True)),
                ('area', models.CharField(max_length=500, null=True)),
                ('description', models.TextField(null=True)),
                ('bloomberg_url', models.CharField(max_length=100, null=True)),
                ('is_bloomberg_scraped', models.BooleanField(default=False)),
                ('last_scraped_bloomberg', models.DateTimeField(null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'contacts',
            },
        ),
        migrations.CreateModel(
            name='ContactScrapeSource',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('source_name', models.CharField(max_length=150, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'contact_scrape_source',
            },
        ),
        migrations.CreateModel(
            name='FeedbackSearchTerm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('search_term', models.CharField(max_length=500)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'feedback_search_term',
            },
        ),
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('organization_name', models.CharField(max_length=150)),
                ('organization_symbol', models.CharField(max_length=50, null=True)),
                ('sector', models.CharField(max_length=50, null=True)),
                ('industry', models.CharField(max_length=50, null=True)),
                ('sub_industry', models.CharField(max_length=50, null=True)),
                ('address', models.CharField(max_length=100, null=True)),
                ('city', models.CharField(max_length=50, null=True)),
                ('state', models.CharField(max_length=50, null=True)),
                ('zipcode', models.CharField(max_length=10, null=True)),
                ('country', models.CharField(max_length=50, null=True)),
                ('phone', models.CharField(max_length=20, null=True)),
                ('website', models.CharField(max_length=50, null=True)),
                ('founded', models.CharField(max_length=50, null=True)),
                ('number_of_employees', models.CharField(max_length=20, null=True)),
                ('bloomberg_url', models.CharField(max_length=150, null=True)),
                ('is_bloomberg_scraped', models.BooleanField(default=False)),
                ('is_yahoo_scraped', models.BooleanField(default=False)),
                ('last_scraped_bloomberg', models.DateTimeField(null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'organizations',
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'tags',
            },
        ),
        migrations.CreateModel(
            name='UserFeedback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('feedback', models.SmallIntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('contact', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_feedback', to='contacts_import.contact')),
                ('feedback_search_term', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_feedback', to='contacts_import.feedbacksearchterm')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'user_feedback',
            },
        ),
        migrations.CreateModel(
            name='SocialProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('platform', models.CharField(max_length=50, null=True)),
                ('platform_link', models.CharField(max_length=500, null=True)),
                ('is_scraped', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('contact', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='social_profiles', to='contacts_import.contact')),
            ],
            options={
                'db_table': 'social_profiles',
            },
        ),
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('school_name', models.CharField(max_length=250)),
                ('school_abbreviation', models.CharField(max_length=10, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('platform', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='schools', to='contacts_import.socialprofile')),
                ('source', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='schools', to='contacts_import.contactscrapesource')),
            ],
            options={
                'db_table': 'schools',
            },
        ),
        migrations.CreateModel(
            name='PersonofInterest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('poi', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contacts_degrees_poi', to='contacts_import.contact')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'persons_of_interests',
            },
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_title', models.CharField(max_length=250, null=True)),
                ('job_start_date', models.CharField(max_length=20, null=True)),
                ('job_end_date', models.CharField(max_length=20, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('contact', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='jobs', to='contacts_import.contact')),
                ('organization', models.ManyToManyField(related_name='organization', to='contacts_import.Organization', verbose_name='organization')),
                ('platform', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='jobs', to='contacts_import.socialprofile')),
                ('source', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='jobs', to='contacts_import.contactscrapesource')),
            ],
            options={
                'db_table': 'jobs',
            },
        ),
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('degree', models.CharField(max_length=200)),
                ('school_start_year', models.CharField(max_length=20, null=True)),
                ('school_end_year', models.CharField(max_length=20, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('contact', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='educations', to='contacts_import.contact')),
                ('platform', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='educations', to='contacts_import.socialprofile')),
                ('school', models.ManyToManyField(related_name='school', to='contacts_import.School', verbose_name='school')),
                ('source', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='educations', to='contacts_import.contactscrapesource')),
            ],
            options={
                'db_table': 'educations',
            },
        ),
        migrations.CreateModel(
            name='ContactTag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('contact', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contact_tags', to='contacts_import.contact')),
                ('tag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cont_tags', to='contacts_import.tag')),
            ],
            options={
                'db_table': 'contact_tags',
            },
        ),
        migrations.CreateModel(
            name='ContactNumber',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact_number_primary', models.CharField(max_length=50, null=True)),
                ('contact_number_secondary', models.CharField(max_length=50, null=True)),
                ('contact_number_tertiary', models.CharField(max_length=50, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('contact', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contact_number', to='contacts_import.contact')),
            ],
            options={
                'db_table': 'contact_numbers',
            },
        ),
        migrations.CreateModel(
            name='ContactMembership',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, null=True)),
                ('company', models.CharField(max_length=50, null=True)),
                ('tenure', models.CharField(max_length=50, null=True)),
                ('membership_type', models.CharField(max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('contact', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contact_memberships', to='contacts_import.contact')),
            ],
            options={
                'db_table': 'contacts_memberships',
            },
        ),
        migrations.CreateModel(
            name='ContactEmail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact_email_primary', models.CharField(max_length=50, unique=True)),
                ('contact_email_secondary', models.CharField(max_length=50, null=True)),
                ('contact_email_tertiary', models.CharField(max_length=50, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('contact', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contact_email', to='contacts_import.contact')),
            ],
            options={
                'db_table': 'contact_emails',
            },
        ),
        migrations.CreateModel(
            name='ContactDescription',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('contact', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contact_description', to='contacts_import.contact')),
                ('platform', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contact_description', to='contacts_import.socialprofile')),
                ('source', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contact_description', to='contacts_import.contactscrapesource')),
            ],
            options={
                'db_table': 'contact_description',
            },
        ),
        migrations.CreateModel(
            name='ContactDegree',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('contact_degree', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contacts_degrees', to='contacts_import.contact')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'contacts_degrees',
            },
        ),
        migrations.AddField(
            model_name='contact',
            name='tags',
            field=models.ManyToManyField(related_name='c_tags', to='contacts_import.Tag'),
        ),
        migrations.AddField(
            model_name='contact',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='contact',
            name='users',
            field=models.ManyToManyField(related_name='contacts', to=settings.AUTH_USER_MODEL),
        ),
    ]