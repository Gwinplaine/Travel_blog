# Generated by Django 3.2 on 2021-06-15 17:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('learning_logs', '0008_comment_date_added'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='date_added',
        ),
    ]
