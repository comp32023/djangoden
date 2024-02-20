# Generated by Django 5.0.1 on 2024-02-20 09:01

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='categories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.TextField()),
            ],
            options={
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.CreateModel(
            name='productinformation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_product', models.CharField(max_length=150, verbose_name='Имя продукта')),
                ('description', models.TextField(blank='None', null=True)),
                ('sale_product', models.IntegerField()),
                ('image_product', models.ImageField(blank=True, null=True, upload_to='')),
                ('image_product2', models.ImageField(blank=True, null=True, upload_to='')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.categories')),
            ],
            options={
                'verbose_name_plural': 'Информация о товарах',
            },
        ),
    ]
