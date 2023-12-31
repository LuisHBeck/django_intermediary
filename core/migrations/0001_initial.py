# Generated by Django 4.2.4 on 2023-08-09 12:43

from django.db import migrations, models
import stdimage.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creation', models.DateField(auto_now_add=True)),
                ('modified', models.DateField(auto_now_add=True)),
                ('active', models.BooleanField(default=True)),
                ('name', models.CharField(max_length=100)),
                ('price', models.DecimalField(decimal_places=2, max_digits=9)),
                ('stock', models.IntegerField()),
                ('image', stdimage.models.StdImageField(force_min_size=False, upload_to='products', variations={'thumb': (124, 124)})),
                ('slug', models.SlugField(blank=True, editable=False, max_length=100)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
