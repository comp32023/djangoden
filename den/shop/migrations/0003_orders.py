# Generated by Django 5.0.1 on 2024-03-03 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_contact'),
    ]

    operations = [
        migrations.CreateModel(
            name='orders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('purchase', models.TextField()),
                ('price', models.IntegerField()),
                ('purchase_note', models.TextField(blank='None', null=True)),
                ('date', models.IntegerField(blank='None', null=True)),
                ('order_status', models.TextField(blank='None', null=True)),
            ],
            options={
                'verbose_name_plural': 'Заказы',
            },
        ),
    ]
