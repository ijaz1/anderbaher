# Generated by Django 4.0.3 on 2022-03-18 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_module', '0010_workassign_work_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='employerdetails',
            name='date_of_birth',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='employerdetails',
            name='id_proof',
            field=models.ImageField(null=True, upload_to='employee_id_proof'),
        ),
    ]
