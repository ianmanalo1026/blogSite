# Generated by Django 3.1.1 on 2020-11-03 07:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogger', '0003_auto_20201101_1733'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='picture',
            field=models.ImageField(default='default.jpg', upload_to='media/'),
        ),
    ]