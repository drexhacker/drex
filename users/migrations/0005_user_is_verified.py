# Generated by Django 2.2.10 on 2020-02-25 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_remove_user_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_verified',
            field=models.BooleanField(default=True),
        ),
    ]