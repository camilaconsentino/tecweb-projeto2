# Generated by Django 4.2.6 on 2023-11-09 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agenda', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contato',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('send_time', models.DateTimeField()),
            ],
        ),
        migrations.DeleteModel(
            name='Agenda',
        ),
    ]
