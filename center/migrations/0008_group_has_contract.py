# Generated by Django 5.1.7 on 2025-04-24 06:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('center', '0007_group_end_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='has_contract',
            field=models.BooleanField(default=False),
        ),
    ]
