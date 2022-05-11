from django.db import models

# Create your models here.


class PartList(models.Model):
    list_name = models.CharField(max_length=250,  verbose_name='Имя для категории')
    mark = models.CharField(max_length=250, verbose_name='Марка')
    list_slug = models.SlugField(max_length=255, verbose_name='slug для категории', unique=True)
    image = models.ImageField(upload_to='images/shop', blank=True)

    class Meta:
        db_table = "Категория запчасти"
        verbose_name_plural = "Категории запчастей"

    def __str__(self):
        return self.list_name


class Category(models.Model):
    part_list = models.ForeignKey(PartList, on_delete=models.CASCADE, blank=True, null=True,  related_name='parent',
                              verbose_name='подкатегория')
    category_name = models.CharField(max_length=250, verbose_name='Название подкатегории',)
    category_slug = models.SlugField(max_length=250, verbose_name='slug поле подкатегории')
    image = models.ImageField(upload_to='images/shop', blank=True)

    def __str__(self):
        return f'{self.category_name} {self.part_list.list_name}'

    def get_slug(self):
        return self.part_list.list_slug

    class Meta:
        db_table = "Категория"
        verbose_name_plural = "Категории"


class Part(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True, related_name='category',
                                 verbose_name='Категория')
    article = models.CharField(max_length=255, verbose_name='Оригинальный артикул')
    article_second = models.CharField(max_length=255, verbose_name='Дополнительный артикул')
    part_name = models.CharField(max_length=255, verbose_name='Наименование')
    part_exist = models.BooleanField(verbose_name='Наличие')
    part_slug = models.SlugField(max_length=250, verbose_name='Слаг')
    part_price = models.IntegerField(verbose_name='Цена запчасти')
    image = models.ImageField(upload_to='images/shop',)

    def __str__(self):
        return f'{self.part_name}:{self.part_price}'

    class Meta:
        db_table = "Деталь"
        verbose_name_plural = 'Детали'
