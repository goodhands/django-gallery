# Generated by Django 4.0.5 on 2022-06-25 21:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0005_alter_photo_description_alter_photo_name_of_creator_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=100, verbose_name='author')),
                ('comment', models.TextField(max_length=1000, verbose_name='comment')),
                ('photo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gallery.photo')),
            ],
        ),
    ]
