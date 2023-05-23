# Generated by Django 4.2.1 on 2023-05-23 20:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_product_size'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='size',
            field=models.CharField(choices=[('30ml', '30ml'), ('50ml', '50ml'), ('100ml', '100ml')], default='None', max_length=10),
        ),
    ]
