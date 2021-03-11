from django.contrib import admin

from .models import Users, Race, CheckPoints


@admin.register(Users)
class UserAdmin(admin.ModelAdmin):
    list_display = ('telegram_id', 'fullname', 'username', 'gender', 'bicycle')


@admin.register(Race)
class RaceAdmin(admin.ModelAdmin):
    list_display = ('fullname', 'start_time', 'finish_time', 'total_time')


@admin.register(CheckPoints)
class CheckPointsAdmin(admin.ModelAdmin):
    list_display = ('name_of_point', 'latitude', 'longitude')
