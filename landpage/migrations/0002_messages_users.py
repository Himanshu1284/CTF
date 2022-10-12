# Generated by Django 3.1.6 on 2021-03-21 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landpage', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Messages_users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Username', models.CharField(max_length=25)),
                ('Email_id', models.EmailField(max_length=254)),
                ('message_by_user', models.TextField()),
                ('date_time', models.TimeField(auto_now=True)),
            ],
        ),
    ]
