# Generated by Django 4.1.7 on 2024-03-02 06:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_person_email_role_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='role',
            name='roletype',
            field=models.CharField(choices=[('EX', 'Executive'), ('CO', 'Councillor'), ('RE', 'Representative'), ('DI', 'Director'), ('OT', 'Other')], max_length=2, null=True),
        ),
    ]