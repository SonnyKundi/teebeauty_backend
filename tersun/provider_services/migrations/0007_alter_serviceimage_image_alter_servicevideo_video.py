# Generated by Django 4.2 on 2023-05-02 20:12

from django.db import migrations, models
import tersun.common.utils


class Migration(migrations.Migration):

    dependencies = [
        ('provider_services', '0006_serviceimage_image_url_servicevideo_video_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='serviceimage',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to=tersun.common.utils.get_directory),
        ),
        migrations.AlterField(
            model_name='servicevideo',
            name='video',
            field=models.FileField(blank=True, null=True, upload_to=tersun.common.utils.get_directory),
        ),
    ]
