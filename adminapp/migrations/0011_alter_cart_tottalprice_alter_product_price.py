# Generated by Django 4.2 on 2023-04-20 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0010_remove_cart_user_cart_users'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='tottalprice',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.PositiveIntegerField(),
        ),
    ]