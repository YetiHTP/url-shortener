# Generated by Django 5.2.3 on 2025-06-16 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shortener', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='url',
            name='short_url',
            field=models.CharField(blank=True, max_length=10, null=True, unique=True),
        ),
    ]
