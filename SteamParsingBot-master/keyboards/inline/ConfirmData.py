from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

confirm_data = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Подтвердить", callback_data="confirm_data")
    ],
    [
        InlineKeyboardButton(text="Ввести заново", callback_data="reset_data")
    ],
])
