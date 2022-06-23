# Generated by Django 4.0.5 on 2022-06-23 19:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(verbose_name='title')),
                ('path', models.TextField(verbose_name='path')),
                ('name_of_creator', models.TextField(verbose_name='creator')),
                ('date_taken', models.DateTimeField(verbose_name='date taken')),
                ('description', models.CharField(max_length=200, verbose_name='description')),
            ],
        ),
    ]
