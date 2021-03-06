# Generated by Django 4.0.3 on 2022-03-17 10:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('admin_module', '0007_employerdetails_photo_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='WorkAssign',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('starting_date', models.CharField(max_length=50)),
                ('ending_date', models.CharField(max_length=50)),
                ('starting_time', models.CharField(max_length=50)),
                ('ending_time', models.CharField(max_length=50)),
                ('client_First_name', models.CharField(max_length=100)),
                ('Client_second_name', models.CharField(max_length=100)),
                ('gender', models.CharField(max_length=50)),
                ('street_address', models.CharField(max_length=500)),
                ('city', models.CharField(max_length=100)),
                ('zip_code', models.CharField(max_length=100)),
                ('additional_information', models.CharField(max_length=3000)),
                ('employer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admin_module.employerdetails')),
            ],
        ),
    ]
