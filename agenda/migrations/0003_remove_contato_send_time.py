# Generated by Django 4.2.6 on 2023-11-09 11:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('agenda', '0002_contato_delete_agenda'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contato',
            name='send_time',
        ),
    ]
