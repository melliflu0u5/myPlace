# Generated by Django 3.2.4 on 2021-07-03 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('signup', '0003_rename_users_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='phone',
            field=models.CharField(max_length=20),
        ),
    ]
