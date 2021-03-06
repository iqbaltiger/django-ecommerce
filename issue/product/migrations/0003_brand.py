# Generated by Django 3.1.6 on 2021-04-06 10:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_auto_20210406_0905'),
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand_name', models.CharField(blank=True, max_length=50, null=True, unique=True)),
                ('brand_image', models.ImageField(default='dummy-profile-pic-male1.webp', null=True, upload_to='images/')),
                ('website', models.CharField(blank=True, max_length=50, null=True, unique=True)),
                ('status', models.BooleanField(default=True)),
            ],
        ),
    ]
