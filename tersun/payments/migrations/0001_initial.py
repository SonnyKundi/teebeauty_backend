# Generated by Django 4.2 on 2023-05-30 20:48

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('providers', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProviderPayment',
            fields=[
                ('id', models.UUIDField(auto_created=True, default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('created_on', models.DateTimeField(db_index=True, default=django.utils.timezone.now, editable=False)),
                ('created_by', models.UUIDField()),
                ('updated_on', models.DateTimeField(db_index=True, default=django.utils.timezone.now)),
                ('updated_by', models.UUIDField()),
                ('is_active', models.BooleanField(default=True)),
                ('amount_paid', models.DecimalField(decimal_places=2, default=0, max_digits=30, validators=[django.core.validators.MinValueValidator(0.0)])),
                ('receipt_number', models.CharField(max_length=300)),
                ('payment_method', models.CharField(choices=[('PDQ', 'PDQ'), ('CASH', 'CASH'), ('CARD', 'CARD'), ('WALLET', 'WALLET'), ('MPESA TILL', 'MPESA TILL'), ('MPESA PAYBILL', 'MPESA PAYBILL'), ('BANK TRANSFER', 'BANK TRANSFER'), ('BANK CHEQUE', 'BANK CHEQUE')], max_length=300)),
                ('payment_code', models.CharField(blank=True, max_length=300, null=True)),
                ('payment_date', models.DateTimeField(db_index=True, default=django.utils.timezone.now)),
                ('provider', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='providers.provider')),
            ],
            options={
                'ordering': ('-updated_on', '-created_on'),
                'abstract': False,
            },
        ),
    ]