# Generated by Django 2.1.2 on 2018-10-07 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CVSection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('section_title', models.CharField(blank=True, max_length=100, null=True)),
                ('section_sequence', models.PositiveSmallIntegerField()),
                ('section_body', models.TextField()),
                ('section_start_date', models.DateField()),
                ('section_end_date', models.DateField(blank=True, null=True)),
            ],
        ),
    ]