# Generated by Django 4.2.3 on 2023-08-20 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_rename_amount_entries_principal'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entries',
            name='due_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]