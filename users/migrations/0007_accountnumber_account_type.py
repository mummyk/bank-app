# Generated by Django 4.2.11 on 2024-11-22 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_alter_accountnumber_updated'),
    ]

    operations = [
        migrations.AddField(
            model_name='accountnumber',
            name='account_type',
            field=models.CharField(default='online', max_length=50),
        ),
    ]
