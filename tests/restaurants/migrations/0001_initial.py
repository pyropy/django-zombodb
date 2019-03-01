# Generated by Django 2.0.13 on 2019-02-12 15:29

import django.contrib.postgres.fields
from django.db import migrations, models
import django_zombodb.indexes
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('tests', '0001_setup_extensions'),
    ]

    operations = [
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('url', models.URLField()),
                ('name', models.TextField()),
                ('street', models.TextField()),
                ('zip_code', models.TextField()),
                ('city', models.TextField()),
                ('state', models.TextField()),
                ('phone', models.TextField()),
                ('email', models.EmailField(max_length=254)),
                ('website', models.URLField(blank=True)),
                ('categories', django.contrib.postgres.fields.ArrayField(base_field=models.TextField(), size=None)),
            ],
        ),
        migrations.CreateModel(
            name='RestaurantNoIndex',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
            ],
        ),
        migrations.AddIndex(
            model_name='restaurant',
            index=models.Index(fields=['url'], name='other-index'),
        ),
        migrations.AddIndex(
            model_name='restaurant',
            index=django_zombodb.indexes.ZomboDBIndex(fields=['name', 'street', 'zip_code', 'city', 'state', 'phone', 'email', 'website', 'categories'], name='restaurants_name_f38813_zombodb'),
        ),
    ]
