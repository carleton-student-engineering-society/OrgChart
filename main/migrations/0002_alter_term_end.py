# Generated by Django 4.1.7 on 2024-02-18 22:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='term',
            name='end',
            field=models.DateField(blank=True, null=True),
        ),
    ]
