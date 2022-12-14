# Generated by Django 3.1.6 on 2021-05-04 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Forensics_challenges',
            fields=[
                ('Challenge_ID', models.CharField(max_length=8, primary_key=True, serialize=False)),
                ('Challenge_Name', models.CharField(max_length=50)),
                ('Challenge_Discription', models.TextField()),
                ('Challenge_Points', models.IntegerField()),
                ('Challenge_Difficulty', models.CharField(choices=[('Easy', 'Easy'), ('Intemediate', 'Intermediate'), ('Hard', 'Hard')], max_length=13)),
                ('Challenge_Answer', models.TextField()),
                ('Challenge_File', models.FileField(null=True, upload_to='')),
                ('Challenge_Ratings', models.IntegerField(default=2.5)),
            ],
        ),
    ]
