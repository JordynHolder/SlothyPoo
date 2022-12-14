# Generated by Django 3.1.5 on 2022-10-07 22:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to='images')),
                ('tags', models.CharField(max_length=200)),
                ('add_date', models.DateTimeField(auto_now_add=True)),
                ('is_nsfw', models.BooleanField()),
            ],
        ),
    ]
