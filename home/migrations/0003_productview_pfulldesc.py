# Generated by Django 2.2.2 on 2020-06-27 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_productview'),
    ]

    operations = [
        migrations.AddField(
            model_name='productview',
            name='pfulldesc',
            field=models.TextField(default=''),
        ),
    ]
