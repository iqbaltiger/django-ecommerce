# Generated by Django 3.1.6 on 2021-04-08 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_brand'),
    ]

    operations = [
        migrations.CreateModel(
            name='Variant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('variant_name', models.CharField(max_length=50, null=True, unique=True)),
                ('variant_status', models.BooleanField(default=True)),
            ],
        ),
        migrations.AlterField(
            model_name='brand',
            name='brand_name',
            field=models.CharField(max_length=50, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='brand',
            name='website',
            field=models.CharField(max_length=50, null=True, unique=True),
        ),
    ]
