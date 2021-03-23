from aiogram.dispatcher.filters.state import State, StatesGroup


class Registration_form(StatesGroup):
    Sex = State()
    Bicycle_type = State()
    Check_data = State()
