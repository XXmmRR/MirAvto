# Generated by Django 4.0.4 on 2022-06-01 07:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0011_alter_order_address_alter_order_created_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='part_exist',
        ),
        migrations.AddField(
            model_name='product',
            name='applicability',
            field=models.CharField(blank=True, max_length=800, null=True, verbose_name='Применяемость'),
        ),
        migrations.AlterField(
            model_name='product',
            name='article',
            field=models.CharField(max_length=255, verbose_name='Оригинальный номер'),
        ),
        migrations.AlterField(
            model_name='product',
            name='article_second',
            field=models.CharField(max_length=255, verbose_name='Производитель'),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Название детали'),
        ),
    ]
