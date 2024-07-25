# Generated by Django 3.0.10 on 2024-07-23 14:16

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
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField(max_length=1000)),
                ('website', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='LogIn',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(default=' ', max_length=200)),
                ('password', models.CharField(default=' ', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='SignIn',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(default=' ', max_length=200)),
                ('last_name', models.CharField(default=' ', max_length=200)),
                ('username', models.CharField(default=' ', max_length=200)),
                ('email', models.EmailField(default=' ', max_length=200)),
                ('password', models.CharField(default=' ', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Jobs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_title', models.CharField(max_length=200)),
                ('location', models.CharField(max_length=200)),
                ('description', models.TextField(max_length=1000)),
                ('requirements', models.TextField(default=' ', max_length=1000)),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='jobs/images/')),
                ('category', models.CharField(max_length=200)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jobs.Company')),
            ],
        ),
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(default=' ', max_length=200)),
                ('last_name', models.CharField(default=' ', max_length=200)),
                ('cover_letter', models.TextField(max_length=200)),
                ('email', models.EmailField(default=' ', max_length=200)),
                ('applied_date', models.DateTimeField(auto_now_add=True)),
                ('applicant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jobs.Jobs')),
            ],
        ),
    ]
