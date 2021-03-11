from django.contrib import admin

from .models import Users, Race, CheckPoints, RacingDate


@admin.register(Users)
class UserAdmin(admin.ModelAdmin):
    list_display = ('telegram_id', 'fullname', 'username', 'gender', 'bicycle')


@admin.register(Race)
class RaceAdmin(admin.ModelAdmin):
    list_display = ('fullname', 'finish_time', 'total_time')


@admin.register(CheckPoints)
class CheckPointsAdmin(admin.ModelAdmin):
    list_display = ('name_of_point', 'latitude', 'longitude')


@admin.register(RacingDate)
class RacingDateAdmin(admin.ModelAdmin):
    display = 'date_of_start'
