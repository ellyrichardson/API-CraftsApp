# Generated by Django 2.1.2 on 2018-12-23 20:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='posts',
            old_name='post_id',
            new_name='id',
        ),
    ]
