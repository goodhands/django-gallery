# Generated by Django 4.0.5 on 2022-07-02 19:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0007_alter_photo_date_taken_alter_photo_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='created_at',
            field=models.DateField(null=True, verbose_name='created date'),
        ),
        migrations.AlterField(
            model_name='photo',
            name='date_taken',
            field=models.DateField(null=True, verbose_name='date taken'),
        ),
        migrations.AlterField(
            model_name='photo',
            name='update_at',
            field=models.DateField(null=True, verbose_name='updated date'),
        ),
    ]