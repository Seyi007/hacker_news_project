# Generated by Django 4.2.4 on 2023-08-13 19:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newsroom', '0004_alter_job_options_alter_story_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='ask',
            options={'ordering': ['-time']},
        ),
    ]
