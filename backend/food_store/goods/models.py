from django.core.validators import MinValueValidator
from django.db import models
from django_resized import ResizedImageField

IMAGE_SIZES = {
    'small': [250, 250],
    'average': [500, 500],
    'big': [1000, 1000],
}


class Category(models.Model):
    """Модель категорий."""
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['name']

    name = models.CharField(
        verbose_name='Наименование',
        max_length=250,
        blank=False,
        unique=True,
        help_text='Наименование категории',
    )
    slug_name = models.SlugField(
        verbose_name='slug-имя',
        max_length=250,
        blank=False,
        unique=True,
        help_text='slug-имя категории',
    )
    image = ResizedImageField(
        verbose_name='Изображение',
        size=IMAGE_SIZES['small'],
        upload_to='images/categories/',
        blank=False,
        help_text='Изображение категории',
    )

    def __str__(self):
        return self.name[:50]


class Subcategory(models.Model):
    """Модель подкатегорий."""
    class Meta:
        verbose_name = 'Податегория'
        verbose_name_plural = 'Подкатегории'
        ordering = ['name']

    name = models.CharField(
        verbose_name='Наименование',
        max_length=250,
        blank=False,
        unique=True,
        help_text='Наименование подкатегории',
    )
    slug_name = models.SlugField(
        verbose_name='slug-имя',
        max_length=250,
        blank=False,
        unique=True,
        help_text='slug-имя подкатегории',
    )
    image = ResizedImageField(
        verbose_name='Изображение',
        size=IMAGE_SIZES['small'],
        upload_to='images/subcategories/',
        blank=False,
        help_text='Изображение подкатегории',
    )
    category = models.ForeignKey(
        Category,
        verbose_name='Категория',
        related_name='subcategories',
        on_delete=models.SET_NULL,
        null=True,
    )

    def __str__(self):
        return self.name[:50]


class UnitOfGoogs(models.Model):
    """Модель товара."""
    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        ordering = ['name']

    name = models.CharField(
        verbose_name='Наименование',
        max_length=250,
        blank=False,
        unique=True,
        help_text='Наименование товара',
    )
    slug = models.SlugField(
        verbose_name='slug-имя',
        max_length=250,
        blank=False,
        unique=True,
        help_text='slug-имя товара',
    )
    image_small = ResizedImageField(
        verbose_name='Изображение малое',
        size=IMAGE_SIZES['small'],
        upload_to='images/goods/small/',
        blank=False,
        help_text='Изображение товара малое',
    )
    image_average = ResizedImageField(
        verbose_name='Изображение среднее',
        size=IMAGE_SIZES['average'],
        upload_to='images/goods/average/',
        blank=False,
        help_text='Изображение товара среднее',
    )
    image_big = ResizedImageField(
        verbose_name='Изображение большое',
        size=IMAGE_SIZES['big'],
        upload_to='images/goods/big/',
        blank=False,
        help_text='Изображение товара большое',
    )
    price = models.DecimalField(
        verbose_name='Цена',
        max_digits=10,
        decimal_places=2,
        validators=(
            MinValueValidator(
                limit_value=0.01,
                message='Цена товара должна быть положительной'
            ),
        ),
        blank=False,
        help_text='Цена товара',
    )
    subcategory = models.ForeignKey(
        Subcategory,
        verbose_name='Податегория',
        related_name='goods',
        on_delete=models.SET_NULL,
        null=True,
    )

    def __str__(self):
        return self.name[:50]
