from django.db import models


class TimedBaseModel(models.Model):
    class Meta:
        abstract = True

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Users(TimedBaseModel):
    class Meta:
        verbose_name = "Участник"
        verbose_name_plural = "Участники"

    telegram_id = models.BigIntegerField(verbose_name="ID телеграм", primary_key=True, unique=True)
    fullname = models.CharField(verbose_name="Имя пользователя", max_length=100, null=True)
    username = models.CharField(verbose_name="Username в телеграм", max_length=100, null=True)
    gender = models.CharField(verbose_name="Пол", max_length=100)
    bicycle = models.CharField(verbose_name="Тип велосипеда", max_length=100)

    def __str__(self):
        return f'{self.fullname} | {self.gender} | {self.bicycle}'


class RacingDate(models.Model):
    class Meta:
        verbose_name = 'Время и дата начала гонки'
        verbose_name_plural = 'Время старта гонки'

    date_of_start = models.DateTimeField(verbose_name="Дата и время старта гонки", null=True, blank=True)

    def __str__(self):
        return f'Дата начала гонки: {self.date_of_start}.'


class Race(models.Model):
    class Meta:
        verbose_name = "Время участника и фото"
        verbose_name_plural = "Время участников и фото"

    fullname = models.ForeignKey(Users, verbose_name="Имя пользователя", on_delete=models.CASCADE,
                                 to_field='telegram_id')
    start_time = models.ForeignKey(RacingDate, verbose_name="Время старта", null=True, on_delete=models.SET_NULL)
    finish_time = models.DateTimeField(verbose_name="Время финиша", auto_now=True)
    total_time = models.DurationField(verbose_name="Время гонки")

    # start_photo = models.ImageField(verbose_name="Фото на старте", upload_to='photos/start')
    # finish_photo = models.ImageField(verbose_name="Фото на финише", upload_to='photos/finish')
    # установить pillows сохранения фото в бд

    def __str__(self):
        return f"{self.fullname} проехал гонку за {self.total_time}"


class CheckPoints(models.Model):
    class Meta:
        verbose_name = "Чек поинт"
        verbose_name_plural = "Чек поинты"

    name_of_point = models.CharField(verbose_name="Название чекпоинта", max_length=255, null=True)
    latitude = models.FloatField(verbose_name="Широта-Х", null=True)
    longitude = models.FloatField(verbose_name="Долгота-Y", null=True)

    def __str__(self):
        return f"{self.name_of_point}:{self.latitude} - {self.latitude}"
