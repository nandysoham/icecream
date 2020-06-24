# Generated by Django 2.2.2 on 2020-06-14 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductView',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pname', models.CharField(max_length=300)),
                ('pcategory', models.CharField(max_length=300)),
                ('psubcategory', models.CharField(max_length=300)),
                ('pdesc', models.CharField(max_length=1000)),
                ('pprice', models.IntegerField()),
                ('pdate', models.DateField()),
            ],
        ),
    ]
