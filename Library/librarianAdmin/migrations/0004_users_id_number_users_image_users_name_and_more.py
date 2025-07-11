# Generated by Django 4.2.20 on 2025-04-08 03:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('librarianAdmin', '0003_bookinghistory_location'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='id_number',
            field=models.CharField(default=0, max_length=100, unique=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='users',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='students/'),
        ),
        migrations.AddField(
            model_name='users',
            name='name',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='users',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
    ]
