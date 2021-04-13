# Generated by Django 3.1.6 on 2021-04-10 10:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0007_auto_20210410_0908'),
    ]

    operations = [
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('supplier_name', models.CharField(max_length=50, null=True)),
                ('supplier_address', models.TextField(blank=True, null=True)),
                ('supplier_mobile', models.CharField(max_length=50, null=True, unique=True)),
                ('supplier_email', models.EmailField(max_length=254, unique=True)),
                ('supplier_details', models.TextField(blank=True, null=True)),
                ('supplier_website', models.CharField(max_length=50, null=True)),
                ('status', models.BooleanField(default=True)),
            ],
        ),
    ]