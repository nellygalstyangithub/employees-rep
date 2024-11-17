# Generated by Django 4.0.8 on 2024-11-12 09:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0009_alter_team_avatar'),
    ]

    operations = [
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='slider')),
                ('title', models.CharField(max_length=255)),
                ('descr', models.TextField(max_length=400)),
                ('link', models.URLField(null=True)),
            ],
        ),
    ]
