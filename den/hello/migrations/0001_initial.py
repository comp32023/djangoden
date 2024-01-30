# Generated by Django 5.0.1 on 2024-01-30 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='categories',
            fields=[
                ('id_category', models.IntegerField(primary_key=True, serialize=False)),
                ('category_name', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='orders',
            fields=[
                ('id_purchase', models.IntegerField(primary_key=True, serialize=False)),
                ('purchase', models.TextField()),
                ('price', models.IntegerField()),
                ('purchase_note', models.TextField(default=0)),
                ('date', models.IntegerField()),
                ('order_status', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='product_information',
            fields=[
                ('id_product', models.IntegerField(primary_key=True, serialize=False)),
                ('name_product', models.CharField(verbose_name=200)),
                ('category_id', models.IntegerField()),
                ('weight', models.TextField(default=0)),
                ('description', models.TextField(default=0)),
                ('structure_goods', models.TextField(default=0)),
                ('possibleboundaries', models.TextField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='sale',
            fields=[
                ('id_sale', models.IntegerField(primary_key=True, serialize=False)),
                ('name_sale', models.CharField(verbose_name=200)),
                ('price', models.IntegerField()),
                ('discounted_price', models.IntegerField(default=0)),
                ('purchase_price', models.IntegerField(default=0)),
                ('provider', models.TextField(default=0)),
                ('note', models.TextField(default=0)),
            ],
        ),
    ]
