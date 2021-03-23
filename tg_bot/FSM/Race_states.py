from aiogram.dispatcher.filters.state import State, StatesGroup


class Race(StatesGroup):
    FIRST_POINT = State()
    CHRIST_THE_SAVIOR = State()
    CATHOLIC_CATHEDRAL = State()
    ALLAAH = State()
    SEYNAGOGUE = State()
    EVANGELICAL = State()
    SCIENTOLOGY = State()
    MOSGORBIKE = State()
    FINISH = State()
