# Generated by Django 5.1.7 on 2025-04-19 14:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('center', '0004_attendance'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='attendance',
            options={'ordering': ['-date']},
        ),
        migrations.RenameField(
            model_name='attendance',
            old_name='present',
            new_name='is_present',
        ),
    ]
