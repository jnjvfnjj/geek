# Generated by Django 4.2.6 on 2023-10-29 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='index',
            name='description',
            field=models.TextField(default=1, verbose_name='описание'),
            preserve_default=False,
        ),
    ]
