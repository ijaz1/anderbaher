# Generated by Django 4.0.3 on 2022-03-11 04:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_module', '0003_alter_category_images_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='category_images',
            name='discription',
            field=models.CharField(max_length=1000, null=True),
        ),
    ]
