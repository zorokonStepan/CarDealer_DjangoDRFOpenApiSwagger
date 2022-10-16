import datetime
from django.db import models
from django.core.validators import MinValueValidator


class CarColor(models.Model):
    color = models.CharField(max_length=50, db_index=True, unique=True, verbose_name='Цвет')

    def __str__(self):
        return self.color

    class Meta:
        verbose_name_plural = 'Цвета'
        verbose_name = 'Цвет'
        ordering = ['id']


class CarBrand(models.Model):
    brand = models.CharField(max_length=25, db_index=True, unique=True, verbose_name='Марка автомобиля')

    def __str__(self):
        return self.brand

    class Meta:
        verbose_name_plural = 'Марки автомобилей'
        verbose_name = 'Марка автомобиля'
        ordering = ['id']


class CarModel(models.Model):
    car_model = models.CharField(max_length=25, db_index=True, unique=True, verbose_name='Модель автомобиля')
    brand = models.ForeignKey('CarBrand', on_delete=models.RESTRICT, verbose_name='Марка автомобиля')

    def __str__(self):
        return self.car_model

    class Meta:
        verbose_name_plural = 'Модели автомобилей'
        verbose_name = 'Модель автомобиля'
        ordering = ['id']


class Order(models.Model):
    order_number = models.AutoField(primary_key=True, verbose_name='Номер заказа')
    color = models.ForeignKey('CarColor', on_delete=models.RESTRICT, verbose_name='Цвет автомобиля')
    car_model = models.ForeignKey('CarModel', on_delete=models.RESTRICT, verbose_name='Модель автомобиля')
    count = models.IntegerField(db_index=True, validators=[MinValueValidator(1)], verbose_name='Количество')
    date = models.DateField(default=datetime.date.today, verbose_name='Дата составления заказа')

    def __str__(self):
        return '-'.join((f'№{str(self.order_number)}',
                         self.car_model.__str__(),
                         self.car_model.brand.__str__(),
                         self.color.__str__(),
                         str(self.count),
                         self.date.strftime('%d.%m.%Y')))

    class Meta:
        verbose_name_plural = 'Заказы'
        verbose_name = 'Заказ'
        ordering = ['date']
