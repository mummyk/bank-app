# Generated by Django 4.2.11 on 2024-11-22 18:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0013_alter_transaction_to_user_localtransfer_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='domestictransfer',
            name='locked',
        ),
    ]
