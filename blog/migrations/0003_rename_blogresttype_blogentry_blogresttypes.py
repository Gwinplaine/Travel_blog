# Generated by Django 3.2 on 2022-06-16 18:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_blogentry_blogresttype'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blogentry',
            old_name='blogresttype',
            new_name='blogresttypes',
        ),
    ]