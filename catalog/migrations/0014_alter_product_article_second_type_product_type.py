# Generated by Django 4.0.4 on 2022-06-09 09:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0013_remove_product_applicability_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='article_second',
            field=models.CharField(max_length=255, verbose_name='Коментарий'),
        ),
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название категории')),
                ('slug', models.SlugField(max_length=250, verbose_name='Слаг')),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='cat', to='catalog.category', verbose_name='Категория')),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='type', to='catalog.type'),
        ),
    ]