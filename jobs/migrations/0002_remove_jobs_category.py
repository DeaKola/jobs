# Generated by Django 3.0.10 on 2024-07-23 14:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='jobs',
            name='category',
        ),
    ]
