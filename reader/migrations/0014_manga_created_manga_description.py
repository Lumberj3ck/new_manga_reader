# Generated by Django 4.2.3 on 2023-09-07 07:39

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('reader', '0013_alter_picture_medium_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='manga',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='manga',
            name='description',
            field=models.TextField(default='07.09.2023'),
            preserve_default=False,
        ),
    ]
