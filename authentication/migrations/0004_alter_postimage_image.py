# Generated by Django 4.2.5 on 2023-10-21 08:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0003_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postimage',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='user/'),
        ),
    ]
