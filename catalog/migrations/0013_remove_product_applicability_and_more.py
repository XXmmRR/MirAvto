# Generated by Django 4.0.4 on 2022-06-03 06:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0012_remove_product_part_exist_product_applicability_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='applicability',
        ),
        migrations.AlterField(
            model_name='product',
            name='article_second',
            field=models.CharField(max_length=255, verbose_name='Применяемость'),
        ),
    ]