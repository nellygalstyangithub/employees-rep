# Generated by Django 4.0.8 on 2024-10-06 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0007_alter_team_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='avatar',
            field=models.ImageField(upload_to='team/'),
        ),
    ]
