# Generated by Django 4.0.8 on 2024-10-04 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0005_team_alter_about_options_alter_contact_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='avatar',
            field=models.ImageField(upload_to='uploads/team'),
        ),
    ]
