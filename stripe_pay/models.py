from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Item(models.Model):
    name = models.CharField(max_length=150, verbose_name='наименование')
    description = models.CharField(max_length=300, verbose_name='описание')
    price = models.PositiveIntegerField(default=0, verbose_name='цена')
    currency = models.CharField(max_length=3, default='USD', verbose_name='валюта')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'


class Order(models.Model):
    items = models.ManyToManyField(Item, verbose_name='продукт')
    total_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='итоговая цена')

    class Meta:
        verbose_name = 'заказ'
        verbose_name_plural = 'заказы'


class Discount(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, verbose_name='заказ')
    amount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='сумма')

    class Meta:
        verbose_name = 'скидка'
        verbose_name_plural = 'скидки'


class Tax(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, verbose_name='заказ')
    amount = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        verbose_name = 'налог'
        verbose_name_plural = 'налоги'
