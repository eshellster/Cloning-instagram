# Generated by Django 2.0.7 on 2018-08-28 22:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0003_auto_20180825_1548'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='image',
            options={'ordering': ['-created_at']},
        ),
    ]