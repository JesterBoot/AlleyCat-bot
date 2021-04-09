from asgiref.sync import sync_to_async

from web.admin_panel.models import Users, Race


@sync_to_async
def add_racer(telegram_id: int, fullname: str, username: str):
    try:
        user = Users(telegram_id=int(telegram_id), fullname=fullname, username=username).save()
        return user
    except:
        return add_racer(int(telegram_id))


# @sync_to_async
# def add_racer(telegram_id: int):
#     user = Users.objects.filter(telegram_id=telegram_id).first()
#     return user


@sync_to_async
def update_racer_gender(gender: str, telegram_id: int):
    gender = Users.objects.filter(telegram_id=telegram_id).update(gender=gender)
    print(gender)


@sync_to_async
def update_racer_bicycle(bicycle: str, telegram_id: int):
    bicycle = Users.objects.filter(telegram_id=telegram_id).update(bicycle=bicycle)
    print(bicycle)


@sync_to_async
def count_racers():
    total_racers = Users.objects.all().count()
    return total_racers


@sync_to_async
def start_time(start_time: 'datetime', telegram_id: int):
    # start_time = Race.start_time
    pass


@sync_to_async
def get_start_time():
    pass


@sync_to_async
def finish_time():
    pass


@sync_to_async
def male_fixie_winners():
    pass


@sync_to_async
def female_fixie_winners():
    pass


@sync_to_async
def male_multispeed_winners():
    pass


@sync_to_async
def female_multispeed_winners():
    pass


@sync_to_async
def all_racers_time():
    pass


@sync_to_async
def delete_racers():
    pass
