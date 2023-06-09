# Generated by Django 4.2 on 2023-05-02 20:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('provider_services', '0007_alter_serviceimage_image_alter_servicevideo_video'),
        ('appointments', '0004_alter_appointment_created_by_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='location',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='provider_services.town'),
        ),
    ]
