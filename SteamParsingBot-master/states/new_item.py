from aiogram.dispatcher.filters.state import State, StatesGroup


class New_Item(StatesGroup):
    New_item = State()
    New_item_price = State()
    Country = State()
    Confirm = State()
