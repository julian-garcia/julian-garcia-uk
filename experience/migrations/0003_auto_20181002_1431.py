# Generated by Django 2.1.1 on 2018-10-02 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('experience', '0002_auto_20181002_1424'),
    ]

    operations = [
        migrations.AddField(
            model_name='experience',
            name='external_link',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='experience',
            name='logo',
            field=models.ImageField(default='#', upload_to=''),
            preserve_default=False,
        ),
    ]
