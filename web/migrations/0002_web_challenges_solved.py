# Generated by Django 3.1.6 on 2021-05-14 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Web_Challenges_solved',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Username', models.CharField(max_length=25)),
                ('Challenge_id', models.CharField(max_length=5)),
            ],
        ),
    ]