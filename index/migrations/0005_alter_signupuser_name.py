# Generated by Django 3.2.4 on 2021-07-03 05:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0004_alter_signupuser_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='signupuser',
            name='name',
            field=models.CharField(max_length=50),
        ),
    ]