# Generated by Django 3.2.5 on 2022-03-10 09:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('icyl_app', '0002_alter_agegroup_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='committee',
            options={'ordering': ['id']},
        ),
    ]
