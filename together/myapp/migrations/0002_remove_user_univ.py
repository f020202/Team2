# Generated by Django 4.0.4 on 2023-02-21 12:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='univ',
        ),
    ]
