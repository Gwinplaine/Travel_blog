# Generated by Django 3.2 on 2021-07-01 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learning_logs', '0015_alter_entry_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='topic',
            name='topicimage',
            field=models.ImageField(blank=True, null=True, upload_to='images'),
        ),
    ]