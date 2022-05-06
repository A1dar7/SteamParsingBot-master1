from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

BotOnStart = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Добавить предмет", callback_data="item")
    ],
])
