# Generated by Django 5.0.1 on 2024-02-02 07:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lms', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='author_photo',
            field=models.ImageField(blank=True, null=True, upload_to='photos'),
        ),
        migrations.AddField(
            model_name='book',
            name='book_photo',
            field=models.ImageField(blank=True, null=True, upload_to='photos'),
        ),
    ]
