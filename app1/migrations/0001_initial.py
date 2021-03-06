# Generated by Django 4.0.3 on 2022-03-11 06:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='get_an_estimate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=100)),
                ('villa_apartment_property', models.CharField(max_length=1000)),
                ('city_zip', models.CharField(max_length=300)),
                ('estimated_budget', models.CharField(max_length=200)),
                ('when_to_start_work', models.CharField(max_length=200)),
            ],
        ),
    ]
