# Generated by Django 4.1 on 2023-08-12 07:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("pssapp", "0006_remove_jobapplications_jobname_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="jobapplications",
            old_name="Job_name",
            new_name="Applied_For",
        ),
    ]
