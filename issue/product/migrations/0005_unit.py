# Generated by Django 3.1.6 on 2021-04-08 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_auto_20210408_1018'),
    ]

    operations = [
        migrations.CreateModel(
            name='Unit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unit_name', models.CharField(max_length=50, null=True, unique=True)),
                ('unit_short_name', models.CharField(max_length=30, null=True, unique=True)),
            ],
        ),
    ]
