# Generated by Django 3.2.5 on 2022-03-11 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('icyl_app', '0008_alter_video_video'),
    ]

    operations = [
        migrations.AddField(
            model_name='prayer',
            name='image',
            field=models.FileField(null=True, upload_to='images/'),
        ),
    ]
