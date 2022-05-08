from aiogram.utils.callback_data import CallbackData
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

Country = CallbackData("id", "country")
choice_country = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="RU", callback_data=Country.new(country='RU'))
    ],
    [
        InlineKeyboardButton(text="US", callback_data=Country.new(country='US'))
    ],
])
