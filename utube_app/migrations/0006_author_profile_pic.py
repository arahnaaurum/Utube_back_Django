# Generated by Django 4.0.6 on 2022-10-23 09:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('utube_app', '0005_alter_video_hashtags'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='profile_pic',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]