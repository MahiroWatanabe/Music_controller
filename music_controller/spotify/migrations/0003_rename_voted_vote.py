# Generated by Django 4.1.5 on 2023-04-20 00:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_room_current_song'),
        ('spotify', '0002_voted'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Voted',
            new_name='Vote',
        ),
    ]
