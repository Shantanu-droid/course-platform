# Generated by Django 5.1.1 on 2024-09-29 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0003_alter_course_image_lessons'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='lessons',
            options={'ordering': ['updated_at']},
        ),
        migrations.AddField(
            model_name='lessons',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
