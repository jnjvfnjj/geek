# Generated by Django 4.2.6 on 2023-11-01 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_index_logo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Photos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_photo', models.ImageField(upload_to='logo_image/', verbose_name='фото на главной странице')),
            ],
        ),
    ]