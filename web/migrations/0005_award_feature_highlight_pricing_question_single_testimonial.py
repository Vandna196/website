# Generated by Django 3.0.3 on 2020-08-12 04:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0004_feature'),
    ]

    operations = [
        migrations.CreateModel(
            name='Award',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='images/')),
                ('isactive', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Feature_highlight',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='images/')),
                ('heading', models.CharField(max_length=255)),
                ('data', models.TextField(max_length=255)),
                ('isactive', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Pricing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('price', models.IntegerField()),
                ('duration', models.CharField(max_length=255)),
                ('link', models.CharField(max_length=255)),
                ('text', models.CharField(max_length=255)),
                ('texta', models.CharField(max_length=255)),
                ('textb', models.CharField(max_length=255)),
                ('isactive', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heading', models.CharField(max_length=255)),
                ('data', models.TextField(max_length=255)),
                ('isactive', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Single_testimonial',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quote', models.TextField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('profile', models.CharField(max_length=255)),
                ('img', models.ImageField(upload_to='images/')),
                ('isactive', models.BooleanField()),
            ],
        ),
    ]
