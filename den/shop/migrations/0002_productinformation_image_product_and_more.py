# Generated by Django 5.0.1 on 2024-02-17 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='productinformation',
            name='image_product',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='productinformation',
            name='sale_product',
            field=models.TextField(blank='None', null=True),
        ),
    ]