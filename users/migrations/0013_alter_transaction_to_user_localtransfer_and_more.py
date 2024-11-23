# Generated by Django 4.2.11 on 2024-11-22 16:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('users', '0012_alter_transaction_transaction_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='to_user',
            field=models.CharField(default='0000000000', max_length=50, verbose_name='beneficiary'),
        ),
        migrations.CreateModel(
            name='LocalTransfer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('beneficiary_bank', models.CharField(max_length=50, verbose_name='beneficiary bank')),
                ('beneficiary', models.CharField(max_length=50, verbose_name='beneficiary')),
                ('beneficiary_account_number', models.BigIntegerField(blank=True, null=True)),
                ('transaction_type', models.CharField(choices=[('current', 'Current Account'), ('saving', 'Saving Account'), ('checking', 'Checking Account')], max_length=50)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=12)),
                ('updated', models.DateTimeField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('locked', models.BooleanField(default=False)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='InternationalTransfer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('beneficiary_name', models.CharField(max_length=200, verbose_name='beneficiary name')),
                ('beneficiary_account_number', models.BigIntegerField(blank=True, null=True)),
                ('transaction_type', models.CharField(choices=[('current', 'Current Account'), ('saving', 'Saving Account'), ('checking', 'Checking Account')], max_length=50)),
                ('beneficiary_bank', models.CharField(max_length=50, verbose_name='beneficiary bank')),
                ('beneficiary_address', models.CharField(max_length=500, verbose_name='beneficiary address')),
                ('country', django_countries.fields.CountryField(max_length=2)),
                ('routing_number', models.CharField(max_length=500, verbose_name='IBAN')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=12)),
                ('reason', models.TextField(max_length=1500, verbose_name='Reason')),
                ('updated', models.DateTimeField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('locked', models.BooleanField(default=False)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='DomesticTransfer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('beneficiary', models.CharField(max_length=50, verbose_name='beneficiary')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=12)),
                ('updated', models.DateTimeField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('locked', models.BooleanField(default=False)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
