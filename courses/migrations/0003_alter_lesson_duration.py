# Generated by Django 4.2 on 2023-04-16 21:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_lesson_description_alter_lesson_youtube_video_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lesson',
            name='duration',
            field=models.DurationField(blank=True, null=True),
        ),
    ]