# Generated by Django 4.0.4 on 2022-05-26 09:19

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0010_alter_order_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='address',
            field=models.CharField(max_length=50, verbose_name='Адресс'),
        ),
        migrations.AlterField(
            model_name='order',
            name='created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Дата создания'),
        ),
        migrations.AlterField(
            model_name='order',
            name='number',
            field=phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None, verbose_name='Номер'),
        ),
        migrations.AlterField(
            model_name='order',
            name='parts',
            field=models.CharField(max_length=2000, verbose_name='Запчасти'),
        ),
        migrations.AlterField(
            model_name='order',
            name='total',
            field=models.DecimalField(decimal_places=2, max_digits=15, verbose_name='Общая цена'),
        ),
    ]
