# Generated by Django 3.2.5 on 2022-03-11 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('icyl_app', '0006_auto_20220311_1040'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='video',
            field=models.CharField(max_length=500),
        ),
    ]
