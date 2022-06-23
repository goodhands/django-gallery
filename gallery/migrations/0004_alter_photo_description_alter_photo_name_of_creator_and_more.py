# Generated by Django 4.0.5 on 2022-06-23 21:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0003_alter_photo_created_at_alter_photo_update_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='description',
            field=models.TextField(max_length=200, verbose_name='description'),
        ),
        migrations.AlterField(
            model_name='photo',
            name='name_of_creator',
            field=models.CharField(max_length=100, verbose_name='creator'),
        ),
        migrations.AlterField(
            model_name='photo',
            name='path',
            field=models.CharField(max_length=100, verbose_name='path'),
        ),
        migrations.AlterField(
            model_name='photo',
            name='title',
            field=models.CharField(max_length=100, verbose_name='title'),
        ),
    ]
