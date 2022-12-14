# Generated by Django 3.1.5 on 2022-10-12 18:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SiteManager', '0002_auto_20221012_1107'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.ImageField(upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='image',
            name='tags',
            field=models.CharField(choices=[('select tag', 'Select Tag'), ('bust', 'Bust'), ('half-Body', 'Half-body'), ('full-Body', 'Full-body')], default='Select Tag', max_length=15),
        ),
    ]
